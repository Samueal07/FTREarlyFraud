import joblib

# Load the trained model from the pickle file
model = joblib.load('fraud_detection_model2.pkl')

# Another sample user prompt to check for prediction
user_prompt = "I received an email saying my bank account was locked, and it included a link to unlock it."

# Use the model to predict whether this is a fraud or safe scenario
prediction = model.predict([user_prompt])[0]  # Returns 1 for fraud, 0 for safe

# Translate prediction to a human-readable label
prediction_label = "Fraud" if prediction == 1 else "Safe"

print("The given prompt is likely to be:", prediction_label)
