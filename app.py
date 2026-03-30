import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load dataset
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
df = pd.read_csv(url)

# Country selector
countries = df['Country/Region'].unique()
selected_country = st.selectbox("Select Country", countries)

st.title(f"COVID Spread Prediction - {selected_country}")

# Filter country data
country_df = df[df['Country/Region'] == selected_country]
country_df = country_df.drop(columns=['Province/State', 'Country/Region', 'Lat', 'Long'])

# Convert to time series
country_series = country_df.sum().reset_index()
country_series.columns = ['Date', 'Cases']
country_series['Date'] = pd.to_datetime(country_series['Date'], format='%m/%d/%y')

# Convert to days
country_series['Days'] = (country_series['Date'] - country_series['Date'].min()).dt.days

# Train model
X = country_series[['Days']]
y = country_series['Cases']

model = LinearRegression()
model.fit(X, y)

# Predict future
future_days = pd.DataFrame({
    'Days': np.arange(X['Days'].max()+1, X['Days'].max()+11)
})

predictions = model.predict(future_days)

# Risk function
def get_risk_level(cases):
    if cases < 10000:
        return "Low"
    elif cases < 100000:
        return "Medium"
    else:
        return "High"

risk_levels = [get_risk_level(c) for c in predictions]

# Show predictions
st.subheader("📊 Predictions for Next 10 Days")

for i in range(len(predictions)):
    st.success(f"Day {i+1}: {int(predictions[i])} cases → {risk_levels[i]} risk")

# Plot graph
st.subheader("📈 Graph")

plt.figure(figsize=(10,5))

# Actual data
plt.plot(country_series['Days'], y, label='Actual')

# Connect last point to predictions
last_day = country_series['Days'].max()
last_case = y.iloc[-1]

extended_days = [last_day] + list(future_days['Days'])
extended_cases = [last_case] + list(predictions)

plt.plot(extended_days, extended_cases, linestyle='dashed', label='Predicted')

plt.legend()
st.pyplot(plt)