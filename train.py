import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

# Load Dataset
df = pd.read_csv("dataset/diabetes.csv")

# Replace invalid zeros in certain medical columns
cols = ["Glucose","BloodPressure","SkinThickness","Insulin","BMI"]
df[cols] = df[cols].replace(0, np.nan)
df.fillna(df.mean(), inplace=True)

# Split
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Train Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("Model trained successfully!")

# Save model + scaler
joblib.dump(model, "model/diabetes_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")
print("Model saved to /model/")
