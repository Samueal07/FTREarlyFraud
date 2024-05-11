import pandas as pd
import numpy as np

# Load the CSV files
fraud_files = ['phishing_scenarios.csv', 'fraud_scenarios.csv', 'sim_swap_scenarios.csv', 'website_spoofing_scenarios.csv']
safe_file = 'safe_scenarios.csv'

# Load fraudulent scenarios
fraud_data = pd.concat([pd.read_csv(file) for file in fraud_files], ignore_index=True)
fraud_data['label'] = 'fraud'  # Label them as fraud

# Load safe scenarios
safe_data = pd.read_csv(safe_file)
safe_data['label'] = 'safe'  # Label them as safe

# Combine the data
data = pd.concat([fraud_data, safe_data], ignore_index=True)
data = data.sample(frac=1).reset_index(drop=True)  # Shuffle the data

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Use TfidfVectorizer to transform text data into numerical features
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
X = vectorizer.fit_transform(data['scenario'])  # Transform the text scenarios into numerical features
y = data['label']  # Labels for the classification

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  # 80% training, 20% testing

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Create a Random Forest classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
rf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf.predict(X_test)

# Calculate accuracy and other metrics
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)
confusion_mat = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Classification Report:\n", classification_rep)
print("Confusion Matrix:\n", confusion_mat)

# Example of a user prompt
user_prompt = ["I got a call from someone claiming to be my bank and asking for my account number."]

# Transform the user prompt using the same vectorizer
user_input = vectorizer.transform(user_prompt)

# Predict whether the user prompt is safe or fraudulent
prediction = rf.predict(user_input)

print("Prediction:", prediction[0])  # Should output 'safe' or 'fraud'

import pickle

# Assuming you've trained the Random Forest model `rf`
# Save the model to a pickle file
with open("fraud_detection_model.pkl", "wb") as f:
    pickle.dump(rf, f)  # Save the model

# Load the model from the pickle file
with open("fraud_detection_model.pkl", "rb") as f:
    loaded_rf = pickle.load(f)  # Load the model

# Test the loaded model with a new user prompt
user_prompt = ["I received an email saying my bank account is suspended and I should click on a link to restore access."]

# Transform the text into numerical features
user_input = vectorizer.transform(user_prompt)

# Make a prediction with the loaded model
prediction = loaded_rf.predict(user_input)

print("Prediction:", prediction[0])  # Output 'safe' or 'fraud'
