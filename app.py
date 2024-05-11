from flask import Flask, request, render_template
import joblib
from pyzbar.pyzbar import decode
from PIL import Image
import pytesseract  # For OCR with Tesseract
import os
import requests
from bs4 import BeautifulSoup
import socket  # For handling network-related errors

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load the machine learning model
model = joblib.load("fraud_detection_model3.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check-results', methods=['POST'])
def check_results():
    user_input = request.form['link']

    # Predict if the scenario is fraud or safe
    prediction = model.predict([user_input])[0]
    prediction_label = "Fraud" if prediction == 1 else "Safe"

    return render_template("results.html", prediction=prediction_label, user_input=user_input)

@app.route('/decode-qr', methods=['POST'])
def decode_qr():
    if 'qr_image' not in request.files:
        return "No file part", 400

    file = request.files['qr_image']
    if file.filename == '':
        return "No selected file", 400

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Decode the QR code
    image = Image.open(file_path)
    decoded_objects = decode(image)

    if not decoded_objects:
        return render_template("results.html", prediction="Could not decode the QR code", user_input="")

    qr_content = decoded_objects[0].data.decode("utf-8")

    is_payment_qr = "upi://" in qr_content.lower()

    if is_payment_qr:
        # Extract payment information and amount
        payment_info = "Payment Requested"
        
        # Find the "am=" parameter in the QR code
        amount = "Unknown"
        for part in qr_content.split("&"):
            if "am=" in part:
                amount = part.split("=")[1]

        return render_template("results.html", 
                               prediction=f"Potential Scam: Payment Request. Amount: {amount}",
                               user_input=qr_content)

    return render_template("results.html", prediction="Decoded QR content", user_input=qr_content)

@app.route('/analyze-url', methods=['POST'])
def analyze_url():
    user_input = request.form['url']

    try:
        response = requests.get(user_input, timeout=10)
        if response.status_code != 200:
            return render_template("results.html", 
                                   prediction=f"Failed to retrieve content. Status code: {response.status_code}", 
                                   user_input=user_input)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        page_content = soup.get_text()

        return render_template("results.html", 
                               prediction="The URL appears safe because content was fetched.", 
                               user_input=user_input,
                               page_content=page_content)

    except (requests.Timeout, requests.ConnectionError, socket.timeout):
        # Treat timeout or connection errors as potential scam indicators
        return render_template("results.html", 
                               prediction="Potential Scam: Unable to fetch content (timeout or connection error).", 
                               user_input=user_input)

    except requests.RequestException as e:
        return render_template("results.html", 
                               prediction=f"Error fetching the URL content: {str(e)}", 
                               user_input=user_input)

@app.route('/analyze-image-text', methods=['POST'])
def analyze_image_text():
    if 'text_image' not in request.files:
        return "No file part", 400

    file = request.files['text_image']
    if file.filename == '':
        return "No selected file", 400

    # Save the uploaded image
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Extract text from the image using Tesseract
    image = Image.open(file_path)
    extracted_text = pytesseract.image_to_string(image)

    # Use the model to predict if the extracted text is fraud or not
    prediction = model.predict([extracted_text])[0]
    prediction_label = "Fraud" if prediction == 1 else "Safe"

    return render_template("results.html", prediction=prediction_label, user_input=extracted_text)
    
if __name__ == '__main__':
    app.run(debug=True)
