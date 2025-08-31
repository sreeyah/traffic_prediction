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
   ```bash
   cd traffic_prediction_text
````

2. Install dependencies:

   ```bash
   pip install flask pandas scikit-learn joblib
   ```

3. Train the model:

   ```bash
   python sample.py
   ```

   This generates a trained model (`model.pkl`).

4. Run Flask app:

   ```bash
   python app.py
   ```

5. Open browser at 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### 🔹 2. Image-based Prediction

1. Navigate to project folder:

   ```bash
   cd traffic_prediction_image
   ```

2. Create and activate virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate      # Mac/Linux
   venv\Scripts\activate         # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run Flask app:

   ```bash
   python traffic_app.py
   ```

5. Open browser at 👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

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

---

## 🖥️ Usage

* **Text-based:** Enter values (humidity, wind speed, pressure, rainfall) and get the predicted temperature.
* **Image-based:** Upload an image → App predicts whether it's **Traffic 🚗** or **No Traffic 🚦**.

---

## 📌 Notes

* Trained CNN model is stored in `traffic_classifier_model.h5`.
* Uploaded images are saved in `uploads/` during runtime.
* Use test images from `test/` to try the app quickly.

---

```

---

👉 Do you want me to also **add screenshots / example images** section in the README so it looks more professional on GitHub?
```
