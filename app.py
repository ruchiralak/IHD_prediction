from flask import Flask, render_template, request
import joblib
import json

app = Flask(__name__)

# Load model and top features
model = joblib.load("random_forest_model.pkl")
with open("top_features.json") as f:
    top_features = json.load(f)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", features=top_features, prediction=None)


@app.route("/predict", methods=["POST"])
def predict():
    input_data = [int(request.form[feature]) for feature in top_features]
    prediction = model.predict([input_data])[0]
    return render_template("index.html", features=top_features, prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
