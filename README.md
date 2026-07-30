# Term-Deposit-Prediction-app
Repository for Term-Deposit-Prediction app

# 📈 Bank Marketing Subscription Prediction

## 🚀 Project Highlights

- Built and evaluated **4 machine learning classification models**
- Conducted comprehensive **Exploratory Data Analysis (EDA)**
- Applied **data preprocessing** and **feature engineering**
- Optimised the final model using **RandomizedSearchCV**
- Selected **Random Forest** as the final deployment model
- Deployed the trained model as an interactive **Streamlit** web application

---

# Project Overview

Direct marketing campaigns are commonly used by banks to promote term deposit subscriptions. However, contacting every customer can be both costly and inefficient. This project develops a machine learning-based decision support system capable of predicting whether a customer is likely to subscribe to a term deposit before a marketing campaign is conducted.

The project follows the complete machine learning development lifecycle, including business understanding, exploratory data analysis (EDA), data preprocessing, model development, feature engineering, hyperparameter tuning, model evaluation, and deployment using Streamlit. Multiple machine learning algorithms were evaluated before selecting the final deployment model based on predictive performance and business suitability.

---

# Business Problem


Banks conduct direct marketing campaigns to encourage customers to subscribe to term deposits. Since marketing resources are limited, contacting every customer may result in unnecessary costs and lower campaign efficiency.

By predicting which customers are more likely to subscribe, banks can prioritise potential customers, improve marketing effectiveness, reduce operational costs, and increase campaign success rates.

This project formulates term deposit subscription prediction as a **binary classification problem**, where the objective is to predict whether a customer will subscribe to a term deposit.

---

# Dataset

This project uses the **Bank Marketing Dataset** obtained from the **UCI Machine Learning Repository**. The dataset contains customer demographic information, previous marketing campaign details, and economic indicators collected from a Portuguese banking institution.

| Attribute | Description |
|-----------|-------------|
| Dataset | Bank Marketing Dataset |
| Source | UCI Machine Learning Repository |
| Number of Records | 41,188 |
| Number of Features | 20 Input Features |
| Target Variable | y |
| Problem Type | Binary Classification |

The dataset was selected because it represents a realistic business problem where financial institutions aim to improve marketing effectiveness using historical customer information.

---

# Exploratory Data Analysis

Exploratory Data Analysis (EDA) was conducted to understand the characteristics of the dataset before model development.

Several important observations were identified, including:

- Distribution of customer demographics
- Marketing campaign characteristics
- Relationships between customer attributes and subscription outcomes
- Correlations among numerical variables
- Class imbalance within the target variable

These findings provided useful business insights and guided the subsequent preprocessing and model development process.

---

# Data Preprocessing

Several preprocessing techniques were applied before training the machine learning models:

- Removed duplicate records
- Removed the `duration` feature to prevent data leakage
- Treated `unknown` values as valid categories
- One-Hot Encoded categorical variables
- Standardised numerical features using StandardScaler
- Split the dataset into training and testing sets

These preprocessing steps ensured that the dataset was suitable for machine learning while preventing information leakage and maintaining consistency during deployment.

---

# Machine Learning Models

Four supervised machine learning algorithms were evaluated in this project:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

The models were compared using appropriate classification metrics to identify the most suitable model for predicting customer subscriptions.

---

# Hyperparameter Tuning

To improve predictive performance, **RandomizedSearchCV** was applied to optimise the Random Forest model by searching for better hyperparameter combinations.

The tuned Random Forest model achieved the best overall performance and was selected as the final deployment model.

---

# Final Model Selection

Although multiple machine learning algorithms were evaluated throughout this project, **Random Forest** was selected as the final deployment model.

The decision was based on:

- Strong overall predictive performance
- Good balance between Precision, Recall and F1-score
- Robust performance on unseen testing data
- Suitability for the business problem

The selected model provides reliable predictions while supporting effective marketing decision-making.

---

# Streamlit Deployment

To demonstrate the practical application of the trained machine learning model, the final Random Forest model was deployed using **Streamlit**.

The web application allows users to enter customer information and instantly receive a prediction indicating whether the customer is likely to subscribe to a term deposit.

### Key Features

- Interactive customer information input
- Real-time subscription prediction
- Prediction probability display
- Business recommendation based on prediction
- User-friendly interface suitable for non-technical users

---

# Application Preview

## Homepage

*(Insert Screenshot Here)*

## Positive Prediction Example

*(Insert Screenshot Here)*

## Negative Prediction Example

*(Insert Screenshot Here)*

---

# Repository Structure

```text
Bank-Marketing-Prediction/
│
├── app.py
├── bank_marketing.ipynb
├── final_random_forest_model.pkl
├── one_hot_encoder.pkl
├── model_feature_columns.pkl
├── requirements.txt
├── README.md
└── screenshots/
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Bank-Marketing-Prediction.git
```

Navigate into the project directory:

```bash
cd Bank-Marketing-Prediction
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

# Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Matplotlib

---

# References

- UCI Machine Learning Repository – Bank Marketing Dataset
- Scikit-learn Documentation
- Streamlit Documentation
- Pandas Documentation
- NumPy Documentation

---

# Conclusion

This project demonstrates how machine learning can support banking institutions in improving the effectiveness of direct marketing campaigns. Through data preprocessing, exploratory data analysis, model comparison, hyperparameter tuning, and deployment, the final Random Forest model provides a practical decision support tool capable of predicting customer subscription likelihood.

The deployed Streamlit application transforms the trained machine learning model into an interactive and user-friendly solution, illustrating how predictive analytics can assist organisations in making more informed, data-driven marketing decisions.

---