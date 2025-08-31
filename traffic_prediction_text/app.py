# app.py
from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            humidity = float(request.form["humidity"])
            wind_speed = float(request.form["wind_speed"])
            pressure = float(request.form["pressure"])
            rainfall = float(request.form["rainfall"])

            features = np.array([[humidity, wind_speed, pressure, rainfall]])
            features_scaled = scaler.transform(features)
            prediction = model.predict(features_scaled)[0]
        except Exception as e:
            prediction = f"Error: {str(e)}"
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
