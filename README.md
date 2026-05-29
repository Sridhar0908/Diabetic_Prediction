# 🩺 Diabetes Prediction System

A Machine Learning + Flask web application that predicts whether a person is diabetic or non-diabetic based on medical input values.

---

# 🚀 Features

* Diabetes prediction using Machine Learning
* User-friendly Flask web interface
* Login & Signup system
* Responsive Bootstrap UI
* Displays prediction result instantly
* Keeps entered values after prediction
* Clear button resets all fields and results

---

# 🛠 Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* HTML/CSS
* Bootstrap
* Joblib

---

# 📂 Project Structure

```bash
Diabetic_Prediction/
│
├── app.py
├── train.py
├── requirements.txt
├── README.md
├── report.pdf
│
├── dataset/
│   └── diabetes.csv
│
├── model/
│   ├── diabetes_model.pkl
│   └── scaler.pkl
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── img/
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── predict.html
│   ├── login.html
│   └── signup.html
│
└── venv/
```

---

# ⚙️ Installation Steps

## 1. Clone Repository

```bash
git clone https://github.com/Sridhar0908/Diabetic_Prediction.git
```

## 2. Open Project Folder

```bash
cd Diabetic_Prediction
```

## 3. Create Virtual Environment

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

### Windows

```bash
.\venv\Scripts\Activate.ps1
```

---

# 📦 Install Required Packages

```bash
pip install -r requirements.txt
```

---

# 📊 Train Machine Learning Model

```bash
python train.py
```

This creates:

* `diabetes_model.pkl`
* `scaler.pkl`

inside the `model/` folder.

---

# ▶️ Run Flask Application

```bash
python app.py
```

Open browser:

```bash
http://127.0.0.1:5000
```

---

# 🧪 Sample Inputs

| Feature           | Value |
| ----------------- | ----- |
| Pregnancies       | 2     |
| Glucose           | 120   |
| Blood Pressure    | 70    |
| Skin Thickness    | 20    |
| Insulin           | 85    |
| BMI               | 28.5  |
| Diabetes Pedigree | 0.5   |
| Age               | 32    |

---

# 📸 Screenshots

## Home Page

![Home](static/img/home.png)

## Prediction Page

![Prediction](static/img/predict.png)

## Result Page

![Result](static/img/result.png)

## Login Page

![Login](static/img/login.png)

---

# 👨‍💻 Author

Sridhar

GitHub:
https://github.com/Sridhar0908

---

# 📄 License

This project is for educational purposes only.
