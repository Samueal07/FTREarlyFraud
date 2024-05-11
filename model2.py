# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split, GridSearchCV
# from sklearn.metrics import classification_report, confusion_matrix

# # Load data from all CSV files
# fraud_data = pd.read_csv("fraud_scenarios.csv")
# phishing_data = pd.read_csv("phishing_scenarios.csv")
# sms_swap_data = pd.read_csv("sim_swap_scenarios.csv")
# website_spoofing_data = pd.read_csv("website_spoofing_scenarios.csv")
# safe_data = pd.read_csv("safe_scenarios.csv")

# # Add a 'label' column to each dataset
# fraud_data['label'] = 'fraud'
# phishing_data['label'] = 'fraud'
# sms_swap_data['label'] = 'fraud'
# website_spoofing_data['label'] = 'fraud'
# safe_data['label'] = 'safe'

# # Concatenate all datasets into a single dataframe
# all_data = pd.concat([fraud_data, phishing_data, sms_swap_data, website_spoofing_data, safe_data], ignore_index=True)

# # Preprocess text data using TF-IDF
# vectorizer = TfidfVectorizer()  # You can tweak the parameters for better performance
# X = vectorizer.fit_transform(all_data['scenario'])  # Assuming 'scenario' is the column with the text
# y = all_data['label']  # The labels ("fraud" or "safe")

# # Split data into training and testing sets (80-20 split)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Create a Random Forest classifier and tune its parameters with GridSearchCV
# param_grid = {
#     "n_estimators": [100, 200, 300],  # Number of trees in the forest
#     "max_features": ["auto", "sqrt", "log2"],  # Number of features to consider at each split
#     "max_depth": [10, 20, None],  # Maximum depth of the trees
# }

# grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=5, scoring="accuracy")
# grid_search.fit(X_train, y_train)  # Train the model with GridSearchCV

# best_rf = grid_search.best_estimator_  # The best Random Forest model from the search

# # Evaluate the model on the test set
# y_pred = best_rf.predict(X_test)

# # Print the confusion matrix and classification report
# print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
# print("Classification Report:\n", classification_report(y_test, y_pred))


import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from joblib import dump
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
# Load your datasets (replace with your CSV file names)
fraud_phishing = pd.read_csv("phishing_scenarios.csv")
fraud_sim_swap = pd.read_csv("sim_swap_scenarios.csv")
fraud_vishing = pd.read_csv("fraud_scenarios.csv")
safe_scenarios = pd.read_csv("safe_scenarios.csv")

# Combine all datasets into a single DataFrame
all_data = pd.concat([fraud_phishing, fraud_sim_swap, fraud_vishing, safe_scenarios], ignore_index=True)

# Assuming there's a 'scenario' column with the description and 'label' column indicating fraud or safe
# If your data structure is different, adjust accordingly
# Example: 1 for 'fraud', 0 for 'safe'
label_encoder = LabelEncoder()
all_data['label'] = label_encoder.fit_transform(all_data['label'])  # 1 = fraud, 0 = safe

# Create a TF-IDF vectorizer for text processing and a Random Forest classifier
pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),  # Convert text to TF-IDF features
    ("classifier", RandomForestClassifier(random_state=42))  # Random Forest with a fixed random state
])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    all_data['scenario'], all_data['label'], test_size=0.2, random_state=42
)

# Train the pipeline
pipeline.fit(X_train, y_train)

# Cross-validation to check consistency
cross_val_results = cross_val_score(pipeline, X_train, y_train, cv=5, scoring='accuracy')
print("Cross-Validation Results:", cross_val_results)
print("Average Accuracy:", np.mean(cross_val_results))

# Test the model on the test set
y_pred = pipeline.predict(X_test)

# Generate the confusion matrix and classification report
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the model to a .pkl file for later use
dump(pipeline, 'fraud_detection_model2.pkl')

with open("fraud_detection_model.pkl", "rb") as f:
    loaded_rf = pickle.load(f)  # Load the model

# Test the loaded model with a new user prompt
user_prompt = ["I received an email saying my bank account is suspended and I should click on a link to restore access."]


