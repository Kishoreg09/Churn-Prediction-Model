# Churn Prediction Project

This project focuses on predicting customer churn for a bank using machine learning. It includes data preprocessing, exploratory data analysis (EDA), feature engineering, model training and evaluation, and deployment using a Streamlit app.

---

## 📁 Folder Structure
<pre> Churn-Prediction-Project/ │ ├── 📁 Notebooks/ │ ├── 1_eda_and_visualization.ipynb │ ├── 2_feature_engineering.ipynb │ └── 3_model_training_and_evaluation.ipynb │ ├── 📁 Models/ │ └── random_forest_model.pkl │ ├── 📁 Data/ │ ├── Churn_Modelling.csv # Original Dataset │ └── processed_churn_data.csv # Cleaned & engineered dataset │ ├── 📄 app.py # Streamlit web app ├── 📄 README.md # Project description └── 📄 requirements.txt # List of dependencies </pre>

---

## Problem Statement

Customer churn (leaving the bank) has a direct impact on business profitability. The objective is to **predict whether a customer will exit** the bank using customer data.

---

##  Dataset Information

The dataset includes the following features:

- CreditScore, Age, Balance, EstimatedSalary
- Gender, Geography
- Tenure, NumOfProducts, HasCrCard, IsActiveMember
- Target Variable: `Exited` (1 = Churned, 0 = Not Churned)

Source: [Kaggle – Churn Modelling Dataset](https://www.kaggle.com/datasets/shubhendra7/churn-modelling)

---

##  Project Stages

### 1️ Exploratory Data Analysis (EDA)
- Distribution plots
- Count plots vs target (`Exited`)
- Boxplots and correlation heatmap

### 2️ Feature Engineering
- Handled missing values (if any)
- Binned Age & Tenure
- One-hot encoded `Geography`
- Label encoded `Gender`
- Created new features like:
  - `BalanceSalaryRatio` = Balance / Salary
  - `AgeTenureRatio` = Age / Tenure

### 3️ Model Training & Evaluation
Trained 4 ML models:
- Logistic Regression
- Decision Tree
- Random Forest  (Best Accuracy)
- XGBoost

Metrics used:
- Accuracy
- Confusion Matrix
- Classification Report (Precision, Recall, F1-score)

Saved best model using `joblib`.

---

##  Deployment (Streamlit)

A simple user interface built with Streamlit that:
- Accepts user input
- Predicts churn
- Displays result in real-time

To run:

```bash
streamlit run app.py
