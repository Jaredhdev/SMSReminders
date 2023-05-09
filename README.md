# SMS Reminders

## Description
A web application that allows users to create reminders and get notified via SMS.

## Technologies Used
- Python 3
- Flask
- Twilio
- ngrok

## Features
- Users can create reminders.
- Users can edit reminders.
- Users can delete reminders.
- Users can get notified via SMS. (In progress)

## Getting Started
1. Create a Twilio account and get a phone number.
2. Clone this repository
    ```
    git clone https://github.com/Jaredhdev/SMSReminders.git
    ```
3. Start a virtual environment
   ```
   cd SMSReminders
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies
   ```
   pip install -r requirements.txt
   ```
5. Run the application
   ```
   python3 main.py
   ```
6. Run ngrok
   ```
   ngrok http 5000
   ```
7. Copy the forwarding URL and append /sms to the end of it.
8. Paste the URL into the Twilio console under the Messaging section.
9. Send a text message to your Twilio number to test it out!
