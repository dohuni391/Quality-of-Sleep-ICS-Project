import tkinter as tk
from tkinter import messagebox
import numpy as np
import joblib
import pandas as pd

# Load the trained model and scaler
model = joblib.load('best_model.pkl')  # Replace with your model file path

# Encoding mappings
encoders_info = {
    'Gender': {'Female': 0, 'Male': 1},
    'Occupation': {'Accountant': 0, 'Doctor': 1, 'Engineer': 2, 'Lawyer': 3, 'Manager': 4,
                   'Nurse': 5, 'Sales Representative': 6, 'Salesperson': 7, 'Scientist': 8,
                   'Software Engineer': 9, 'Teacher': 10},
    'BMI Category': {'Normal': 0, 'Obese': 1, 'Overweight': 2},
    'Blood Pressure': {'Hypertension': 0, 'Normal': 1, 'Prehypertension': 2},
    'Sleep Disorder': {'Insomnia': 0, 'None': 1, 'Sleep Apnea': 2},
}

# Function to encode user inputs
def encode_user_input(user_input):
    encoded_values = []
    for feature, value in user_input.items():
        if feature in encoders_info:  # Encode categorical data
            try:
                encoded_values.append(encoders_info[feature][value])
            except KeyError:
                raise ValueError(f"Invalid input for {feature}. Allowed values: {list(encoders_info[feature].keys())}")
        else:  # Numerical data, add directly
            encoded_values.append(float(value))

    feature_names = list(user_input.keys())
    df = pd.DataFrame([encoded_values], columns=feature_names)
    return df

# Function to predict sleep quality
def predict_sleep_quality():
    try:
        # Get user input
        user_input = {
            'Gender': gender_var.get(),
            'Age': int(age_entry.get()),
            'Occupation': occupation_var.get(),
            'Sleep Duration': float(sleep_duration_entry.get()),
            'Physical Activity Level': int(physical_activity_entry.get()),
            'Stress Level': int(stress_level_entry.get()),
            'BMI Category': bmi_category_var.get(),
            'Blood Pressure': blood_pressure_var.get(),
            'Heart Rate': int(heart_rate_entry.get()),
            'Daily Steps': int(daily_steps_entry.get()),
            'Sleep Disorder': sleep_disorder_var.get(),
        }

        # Encode input
        encoded_input = encode_user_input(user_input)

        # Predict
        prediction = model.predict(encoded_input)

        # Display result
        messagebox.showinfo("Prediction", f"Predicted Quality of Sleep: {prediction[0]:.2f}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")

# Create the GUI application
root = tk.Tk()
root.title("Sleep Quality Predictor")

# Define input fields
gender_var = tk.StringVar()
occupation_var = tk.StringVar()
bmi_category_var = tk.StringVar()
blood_pressure_var = tk.StringVar()
sleep_disorder_var = tk.StringVar()

tk.Label(root, text="Gender (Male/Female):").grid(row=0, column=0)
tk.Entry(root, textvariable=gender_var).grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

tk.Label(root, text="Occupation (e.g., Engineer, Teacher):").grid(row=2, column=0)
tk.Entry(root, textvariable=occupation_var).grid(row=2, column=1)

tk.Label(root, text="Sleep Duration (hours):").grid(row=3, column=0)
sleep_duration_entry = tk.Entry(root)
sleep_duration_entry.grid(row=3, column=1)

tk.Label(root, text="Physical Activity Level (min):").grid(row=4, column=0)
physical_activity_entry = tk.Entry(root)
physical_activity_entry.grid(row=4, column=1)

tk.Label(root, text="Stress Level (1-10):").grid(row=5, column=0)
stress_level_entry = tk.Entry(root)
stress_level_entry.grid(row=5, column=1)

tk.Label(root, text="BMI Category (Normal/Overweight/Obese):").grid(row=6, column=0)
tk.Entry(root, textvariable=bmi_category_var).grid(row=6, column=1)

tk.Label(root, text="Blood Pressure (Normal/Prehypertension/Hypertension):").grid(row=7, column=0)
tk.Entry(root, textvariable=blood_pressure_var).grid(row=7, column=1)

tk.Label(root, text="Heart Rate:").grid(row=8, column=0)
heart_rate_entry = tk.Entry(root)
heart_rate_entry.grid(row=8, column=1)

tk.Label(root, text="Daily Steps:").grid(row=9, column=0)
daily_steps_entry = tk.Entry(root)
daily_steps_entry.grid(row=9, column=1)

tk.Label(root, text="Sleep Disorder (None/Insomnia/Sleep Apnea):").grid(row=10, column=0)
tk.Entry(root, textvariable=sleep_disorder_var).grid(row=10, column=1)

# Predict button
tk.Button(root, text="Predict", command=predict_sleep_quality).grid(row=11, column=0, columnspan=2)

# Run the application
root.mainloop()
