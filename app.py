from flask import Flask, render_template, request, session, redirect, url_for, flash
import numpy as np
import joblib
import webbrowser
import threading
import time 
import os # <-- IMPORT ADDED HERE

# --- Configuration ---
app = Flask(__name__)
# IMPORTANT: This secret key is necessary for session management (used in base.html)
app.secret_key = 'your_super_secret_key_here' 

# Mock User Data (Replace with a proper database in a real app)
MOCK_USERS = {
    "test@medicare.com": {
        "password": "password",
        "first_name": "Test",
        "last_name": "User"
    }
}
# --- Model Loading ---
try:
    # Assuming model and scaler files exist in 'model/'
    model = joblib.load("model/diabetes_model.pkl")
    scaler = joblib.load("model/scaler.pkl")
except FileNotFoundError:
    print("Warning: Model files not found. Prediction route will not work.")
    model = None
    scaler = None


# --- Function to Open Browser ---
def open_browser():
    # Wait 1 second before opening browser to ensure server is ready
    time.sleep(1) 
    webbrowser.open("http://127.0.0.1:5000/")


# --- Core Routes ---

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "GET":
        return render_template("predict.html")
    
    if model is None or scaler is None:
        flash("Error: Prediction model not loaded.", "danger")
        return render_template("predict.html")

    # POST handling for prediction
    try:
        fields = [
            "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
            "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
        ]
        data = [float(request.form[field]) for field in fields]
    except ValueError:
        flash("Invalid input. Please enter numbers for all fields.", "warning")
        return render_template("predict.html", prediction="Invalid input. Please enter numbers.")

    arr = np.array(data).reshape(1, -1)
    arr_scaled = scaler.transform(arr)
    prediction = model.predict(arr_scaled)[0]
    result = "Diabetic" if prediction == 1 else "Not Diabetic"

    return render_template("predict.html", prediction=result)

# --- Authentication Routes ---
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user_info = MOCK_USERS.get(email)
        if user_info and user_info['password'] == password:
            session['user'] = user_info['first_name']
            session['email'] = email
            flash(f"Welcome back, {session['user']}!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login failed. Check your email and password.", "danger")
            return render_template("login.html")
    if session.get('user'):
        return redirect(url_for('home'))
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if email in MOCK_USERS:
            flash("This email is already registered.", "warning")
            return render_template("signup.html")

        if password != confirm_password:
            flash("Passwords do not match.", "warning")
            return render_template("signup.html")

        MOCK_USERS[email] = {
            "password": password,
            "first_name": first_name,
            "last_name": request.form.get("last_name")
        }
        
        session['user'] = first_name
        session['email'] = email
        
        flash("Account created successfully! You are now logged in.", "success")
        return redirect(url_for("home"))

    return render_template("signup.html")

@app.route("/logout")
def logout():
    session.pop('user', None)
    session.pop('email', None)
    flash("You have been logged out.", "info")
    return redirect(url_for("home"))

@app.route("/dashboard")
def dashboard():
    if not session.get('user'):
        flash("You need to log in to access the dashboard.", "warning")
        return redirect(url_for('login'))
    
    return "<h1>Dashboard (Requires dashboard.html)</h1>" # Simple response since dashboard.html is missing


# --- App Execution (The part that auto-launches) ---
if __name__ == "__main__":
    # Check for the WERKZEUG_RUN_MAIN environment variable.
    # It is set to 'true' in the reloader subprocess, which we want to ignore.
    if not os.environ.get('WERKZEUG_RUN_MAIN'):
        # This line ensures the browser is launched 1 second after the app starts
        threading.Timer(1.0, open_browser).start() 
        
    app.run(debug=True)