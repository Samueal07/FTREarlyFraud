# GuardTrust: Advanced Real-Time Fraud Detection System

GuardTrust is an advanced real-time fraud detection system designed to prevent fraud before it occurs. The system is deployed using Flask for the backend and HTML, CSS, and JavaScript for the frontend. It can analyze various types of input to detect potential fraud, including URLs, Email/SMS messages, QR codes, and messages from popular banks.

## Features

- **URL Analysis**: Detects shortened and encrypted URLs using a phishing dataset from Kaggle.
- **Email/SMS Fraud Detection**: Analyzes messages for potential fraud.
- **QR Code Scanning**: Identifies fraudulent QR codes.
- **Bank Message Verification**: Checks the legitimacy of messages from popular banks.
- **Credit Card Fraud Detection**: Uses an IBM dataset of over 6 million transactions to analyze spending patterns.

## Data Collection

- Built from scratch using web scraping and manual collection of legitimate and non-legitimate examples.
- URL analysis model trained with a phishing dataset from Kaggle.
- Credit card fraud detection model developed using an IBM dataset.

## Installation

To get started with GuardTrust, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/GuardTrust.git
   cd GuardTrust
