'''
     -----linear regression--------------------------------
import tkinter as tk
from sklearn.linear_model import LinearRegression
import numpy as np

# Sample data for training
X = np.array([[1000, 2], [1200, 3], [1500, 4], [1800, 5], [2000, 6]])  # sqft, bedrooms
y = np.array([3000000, 4000000, 6000000, 8000000, 10000000])  # price

# Train linear regression model
model = LinearRegression()
model.fit(X, y)

def calculate_price():
    sqft = float(entry_sqft.get())
    bedrooms = float(entry_bedrooms.get())
    location = location_var.get()

    # Adjust price based on location (optional)
    if location == "Chennai":
        location_factor = 1.2
    elif location == "Outer Chennai":
        location_factor = 0.8
    else:
        location_factor = 1

    # Predict price using linear regression model
    predicted_price = model.predict(np.array([[sqft, bedrooms]]))[0] * location_factor

    # Display predicted price
    label_result.config(text=f"Predicted Price: ₹{predicted_price:.2f} Lakhs")

# Create GUI
window = tk.Tk()

window.title("Property Price Predictor")

tk.Label(window, text="Square Feet:").grid(row=0, column=0)
entry_sqft = tk.Entry(window)
entry_sqft.grid(row=0, column=1)

tk.Label(window, text="Bedrooms:").grid(row=1, column=0)
entry_bedrooms = tk.Entry(window)
entry_bedrooms.grid(row=1, column=1)

tk.Label(window, text="Location:").grid(row=2, column=0)
location_var = tk.StringVar()
location_var.set("Select Location")  # default value
options = ["Select Location", "Chennai", "Outer Chennai"]
location_menu = tk.OptionMenu(window, location_var, *options)
location_menu.grid(row=2, column=1)

button_calculate = tk.Button(window, text="Calculate Price", command=calculate_price)
button_calculate.grid(row=3, column=0, columnspan=2)

label_result = tk.Label(window, text="")
label_result.grid(row=4, column=0, columnspan=2)

window.mainloop()

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor  # Use Regressor instead of Classifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.tree import export_text

# Dataset
data = {
    'Age': [22, 23, 24, 22, 23, 24, 25, 22, 23, 24],
    'Experience': [0, 0.5, 1, 0, 0.5, 1, 1.5, 0, 0.5, 1],
    'Technology': ['Python', 'Java', 'JavaScript', 'Data Science', 'Python', 'Java', 'JavaScript', 'Machine Learning', 'Data Science', 'Machine Learning'],
    'Salary': [60000, 55000, 50000, 65000, 60000, 55000, 50000, 70000, 65000, 70000]  # Salary based on technology
}

# Create DataFrame
df = pd.DataFrame(data)

# Encode categorical variables
le = LabelEncoder()
df['Technology'] = le.fit_transform(df['Technology'])

# Features and Target (Salary is the target)
X = df[['Age', 'Experience', 'Technology']]
y = df['Salary']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the DecisionTreeRegressor (for predicting continuous values like Salary)
regressor = DecisionTreeRegressor()



# Train the model
regressor.fit(X_train, y_train)

# Make predictions
y_pred = regressor.predict(X_test)

# Calculate the Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Display the decision tree rules
tree_rules = export_text(regressor, feature_names=list(X.columns))
print("\nDecision Tree Rules:")
print(tree_rules)

# Sample prediction (correct format)
sample_data = pd.DataFrame([[24, 2, 2]], columns=['Age', 'Experience', 'Technology'])

# Make prediction for sample data
salary_prediction = regressor.predict(sample_data)
print("\nSample Salary Prediction:", salary_prediction[0])'''

from sklearn.feature_selection import f_classif
import pandas as pd

# Example Data
df = pd.DataFrame({
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [5, 4, 3, 2, 1],
    'Target': [0, 1, 0, 1, 0]
})

X = df[['Feature1', 'Feature2']]
y = df['Target']

# ANOVA F-test
f_values, p_values = f_classif(X, y)
for i, p in enumerate(p_values):
    print(f"Feature {i+1}: P-Value = {p}")
