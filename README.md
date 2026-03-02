🔹 Project Title

Customer Churn Prediction System using Machine Learning

🔹 Problem Statement

Explain business problem:

Telecom companies lose customers

Need predictive model to identify churn risk

🔹 Objectives

Build ML classification model

Predict churn probability

Deploy as web application

Provide business insights

🔹 Dataset Description

Features used

Target variable (Churn)

Data source

🔹 Tech Stack

Python

Pandas, NumPy

Scikit-learn

Flask

HTML/CSS

Render (Deployment)

🔹 ML Pipeline

Data Cleaning

EDA

Feature Engineering

Model Training

Evaluation (ROC-AUC, Accuracy)

Model Saving (.pkl)

Deployment

🔹 Model Performance

Mention:

Accuracy

ROC-AUC

Confusion Matrix

🔹 Deployment Link (after Render)
🔹 Folder Structure
customer-churn-capstone/
│
├── README.md
│
├── data/
│   ├── raw/
│   │   └── customer_churn.csv
│   └── processed/
│       └── churn_cleaned.csv
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_model_building.ipynb
│   └── 05_model_evaluation.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── models/
│   └── churn_model.pkl
│
├── reports/
│   ├── business_report.pdf
│   ├── technical_documentation.pdf
│   └── model_metrics.csv
│
├── deployment/
│   ├── app.py
│   ├── requirements.txt
│   ├── Procfile
│   └── templates/
│       └── index.html
│
├── presentation/
│   └── churn_presentation.pptx
│
└── screenshots/
    └── app_demo.png