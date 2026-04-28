This repo covers **both text-based** and **image-based** traffic prediction projects.

# 🚦 Traffic Prediction Projects

This repository contains two different machine learning projects for **traffic prediction**:

1. **Text-based Traffic Prediction** → Predicts **temperature** (or traffic condition) based on features like humidity, wind speed, pressure, and rainfall.  
2. **Image-based Traffic Prediction** → Classifies uploaded images as **Traffic** or **No Traffic** using a CNN model.

---

## 📂 Project Structure

```

.
├── traffic\_prediction\_text/
│   ├── sample.py              # ML training & prediction script
│   ├── app.py                 # Flask app for text-based input
│   ├── weather\_data.csv       # Dataset
│   ├── static/
│   │   └── style.css          # CSS styling
│   └── templates/
│       └── index.html         # Frontend form

├── traffic\_prediction\_image/
│   ├── traffic\_app.py               # Flask app (main entry point)
│   ├── traffic\_classifier\_model.h5  # Pre-trained CNN model
│   ├── requirements.txt             # Dependencies
│   ├── static/
│   │   └── style.css                # CSS styling
│   ├── templates/
│   │   ├── index.html               # Upload form
│   │   └── result.html              # Result page
│   ├── uploads/                     # Stores uploaded images
│   └── test/                        # Sample test images

````

---

## ⚡ Setup & Installation

### 🔹 1. Text-based Prediction

1. Navigate to project folder:
bash
   cd traffic_prediction_text


2. Install dependencies:

   pip install flask pandas scikit-learn joblib


3. Train the model:

   
   python sample.py
   

   This generates a trained model (`model.pkl`).

4. Run Flask app:

   
   python app.py
   

5. Open browser at 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)



### 🔹 2. Image-based Prediction

1. Navigate to project folder:

   cd traffic_prediction_image


2. Create and activate virtual environment (recommended):


   python -m venv venv
   source venv/bin/activate      # Mac/Linux
   venv\Scripts\activate         # Windows


3. Install dependencies:


   pip install -r requirements.txt


4. Run Flask app:

   python traffic_app.py


5. Open browser at 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)


## Outputs 

 <img width="1298" height="1064" alt="Screenshot 2026-04-28 142546" src="https://github.com/user-attachments/assets/e9aa5b0e-453a-4aac-b30d-3f2daedde3e3" />
                  <img width="568" height="606" alt="Screenshot 2026-04-28 142632" src="https://github.com/user-attachments/assets/fea7b20e-ece0-454a-9426-82ada98c35da" />
                  <img width="611" height="555" alt="Screenshot 2026-04-28 142659" src="https://github.com/user-attachments/assets/6cd0f12a-3514-4351-a711-caa38ddcf7c8" />



## 📦 Requirements

### For Text-based

* Flask
* Pandas
* Scikit-learn
* Joblib

### For Image-based

* Flask
* TensorFlow / Keras
* NumPy
* Pillow
* Werkzeug



## 🖥️ Usage

* **Text-based:** Enter values (humidity, wind speed, pressure, rainfall) and get the predicted temperature.
* **Image-based:** Upload an image → App predicts whether it's **Traffic 🚗** or **No Traffic 🚦**.



## 📌 Notes

* Trained CNN model is stored in `traffic_classifier_model.h5`.
* Uploaded images are saved in `uploads/` during runtime.
* Use test images from `test/` to try the app quickly.

