from flask import Flask, render_template, request
import joblib
import pandas as pd
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "..", "models", "churn_model.pkl")

model = joblib.load(model_path)

app = Flask(__name__)

# Load model and feature columns
model = joblib.load("../models/churn_model.pkl")
feature_columns = joblib.load("../models/feature_columns.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.form.to_dict()

    # Convert numeric fields
    data["Tenure"] = int(data["Tenure"])
    data["MonthlyCharges"] = int(data["MonthlyCharges"])
    data["TotalCharges"] = int(data["TotalCharges"])
    data["SeniorCitizen"] = int(data["SeniorCitizen"])

    input_df = pd.DataFrame([data])

    # One-hot encode
    input_df = pd.get_dummies(input_df)

    # Match training columns
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    result = "Customer Will Churn" if prediction == 1 else "Customer Will Not Churn"

    return render_template(
        "index.html",
        prediction_text=result,
        probability=round(probability * 100, 2)
    )

if __name__ == "__main__":
    app.run(debug=True)