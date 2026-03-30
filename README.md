# 🌍 COVID-19 Spread Prediction App

A simple Machine Learning web app that predicts COVID-19 case trends for different countries using Linear Regression.

🚀 **Live App:** https://covid-prediction-app-nqy97tou7usopjryxsbsr9.streamlit.app/

---

## 📌 Features

* 🌎 Select any country from dropdown
* 📊 View past COVID-19 case trends
* 🔮 Predict next 10 days cases
* ⚠️ Risk level classification (Low / Medium / High)
* 📈 Graph visualization of actual vs predicted data

---

## 🛠️ Tech Stack

* **Python**
* **NumPy** – numerical operations
* **Pandas** – data handling
* **Matplotlib** – data visualization
* **Scikit-learn** – Linear Regression model
* **Streamlit** – web app framework

---

## 📂 Dataset Used

* Johns Hopkins University COVID-19 Dataset
  🔗 https://github.com/CSSEGISandData/COVID-19

---

## ⚙️ How It Works

1. Load COVID-19 dataset
2. Filter data based on selected country
3. Convert date into numerical format (days)
4. Train Linear Regression model
5. Predict future cases for next 10 days
6. Display predictions with risk levels
7. Plot actual vs predicted graph

---

## 🧠 Machine Learning Concepts Used

* Supervised Learning
* Linear Regression
* Feature Engineering (Date → Days)
* Model Training & Prediction

---

## ▶️ Run Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/Debsmita2005G/covid-prediction-app.git
cd covid-prediction-app
```

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the app

```bash
streamlit run app.py
```

---

## 📦 Requirements

Make sure you have Python installed, then install:

```txt
streamlit
pandas
numpy
matplotlib
scikit-learn
```

---

 Acknowledgements

* Johns Hopkins University for dataset
* Open-source libraries used in this project

---

 Author

**Debsmita Ghosh**
🔗 GitHub: https://github.com/Debsmita2005G

---

Future Improvements

* Add advanced ML models (ARIMA, LSTM)
* Improve prediction accuracy
* Add more visualizations
* Deploy using full-stack (React + Flask)

---
