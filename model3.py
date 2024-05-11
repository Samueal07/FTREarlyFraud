import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Load fraud scenarios from CSV files
fraud_scenarios_1 = pd.read_csv("phishing_scenarios.csv")
fraud_scenarios_2 = pd.read_csv("sim_swap_scenarios.csv")
fraud_scenarios_3 = pd.read_csv("fraud_scenarios.csv")
fraud_scenarios_4 =pd.read_csv("website_spoofing_scenarios.csv")
safe_scenarios = pd.read_csv("safe_scenarios.csv")

# Load safe scenarios from the CSV file
safe_scenarios = pd.read_csv('safe_scenarios.csv')
# Concatenate all data into a single DataFrame
all_scenarios = pd.concat([fraud_scenarios_1, fraud_scenarios_2, fraud_scenarios_3, fraud_scenarios_4, safe_scenarios])

# Check the content of the 'scenario' column to ensure it's text
print("Sample scenarios:", all_scenarios['scenario'].head())

# Create training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    all_scenarios['scenario'], all_scenarios['label'], test_size=0.2, random_state=42
)

# Create a pipeline with TF-IDF for text conversion and Random Forest for classification
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),  # Convert text to numerical representation
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42))
])

# Train the model with the training data
pipeline.fit(X_train, y_train)

# Test the model with the test set
y_pred = pipeline.predict(X_test)

# Generate a classification report to assess accuracy
print("Classification report:")
print(classification_report(y_test, y_pred))

# Save the trained model to a pickle file for future use
joblib.dump(pipeline, 'fraud_detection_model3.pkl')
