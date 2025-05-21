from flask import Flask, request, jsonify, render_template
import joblib
import json
import numpy as np

app = Flask(__name__)

# Load model and features
model = joblib.load("random_forest_model.pkl")
with open("top_features.json") as f:
    top_features = json.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_json = request.get_json()
        input_data = [float(input_json[feat]) for feat in top_features]
    except Exception as e:
        return jsonify({"error": f"Invalid input: {str(e)}"}), 400

    proba = model.predict_proba([input_data])[0][1]
    percent = round(proba * 100, 2)

    if percent >= 60:
        risk = "High Risk"
        message = "⚠️ Medical intervention  necessary."
        color = "red"
    elif percent >= 30:
        risk = "Moderate Risk"
        message = "🟡 Consider medical consultation."
        color = "orange"
    else:
        risk = "Low Risk"
        message = "✅ You appear to be at low risk."
        color = "green"

    return jsonify({
        "probability": percent,
        "risk": risk,
        "message": message,
        "color": color
    })


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)
