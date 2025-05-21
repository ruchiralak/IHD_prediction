# 🫀 Ischemic Heart Disease (IHD) Risk Prediction Web App

This is a simple web application that predicts the risk of Ischemic Heart Disease (IHD) based on user lifestyle and symptom data. The app uses a machine learning model (Random Forest) trained on health-related features and is built with **Flask (Python)** for the backend and **HTML/CSS** for the frontend.

---

## 🚀 Features

- Predicts IHD risk using lifestyle and symptom data
- Loads a `.pkl` model file and `.json` configuration
- Web-based user interface (HTML form)
- Lightweight Flask backend

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (optional: JS)
- **Model**: Scikit-learn (Random Forest)
- **Deployment Ready**: Can be hosted on Render, Railway, or any cloud platform

---

## 📁 Project Structure

.
├── app.py # Flask application
├── model.pkl # Trained ML model
├── config.json # Optional config file (e.g., feature mappings)
├── templates/
│ └── index.html # Frontend page
├── requirements.txt # Python dependencies
└── README.md # Project description


---

## 🧪 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/ruchiralak/IHD_prediction.git
   cd IHD_prediction

2.Install dependencies
   
3.Run the app
    python app.py

4.Open in browser
  http://127.0.0.1:5000


  🧠 How It Works
The user enters lifestyle and symptom-related data into a form.

The Flask backend processes this data and passes it to the pre-trained ML model.

The model outputs a prediction: high or low risk.

The result is displayed on the same web page.

🙋‍♂️ Author
Ruchira Lakshan
Undergraduate Software Engineer
Sri Lanka


