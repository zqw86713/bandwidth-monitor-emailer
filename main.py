import requests
import json
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv


load_dotenv()  # Loads .env from the same directory as main.py

# Define the URL for the bandwidth counter
URL = os.getenv("SERVER_URL", "https://example.com/bandwidth")  # Replace with your actual URL

# Environment variables
sender_email = os.getenv("SMTP_SENDER_EMAIL")
sender_password = os.getenv("SMTP_SENDER_PASSWORD")
recipient_emails_env = os.getenv("RECIPIENT_EMAILS", "")

# Handle recipient emails
if "," in recipient_emails_env:
    recipient_emails = [email.strip() for email in recipient_emails_env.split(",")]
else:
    recipient_emails = [recipient_emails_env.strip()] if recipient_emails_env.strip() else []

# Get the current script directory path (cross-platform)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set the path for the log file
log_file_path = os.path.join(script_dir, "bandwidth_log.txt")

# Function to fetch bandwidth data
def fetch_bandwidth():
    try:
        response = requests.get(URL)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        data = response.json()  # Assuming the response is JSON
        convert_to_gb_and_log(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching bandwidth data: {e}")
    except json.JSONDecodeError:
        print("Error decoding JSON response.")

# Function to convert values to GB, log data, and send email
def convert_to_gb_and_log(data):
    try:
        # Convert bytes to GB
        monthly_limit_gb = data["monthly_bw_limit_b"] / (1024 ** 3)
        bw_counter_gb = data["bw_counter_b"] / (1024 ** 3)

        # Prepare log entry
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = (
            f"{timestamp} - Bandwidth Data (in GB):\n"
            f"  Monthly Limit: {monthly_limit_gb:.2f} GB\n"
            f"  Used: {bw_counter_gb:.2f} GB\n"
            f"  Reset Day: {data['bw_reset_day_of_month']}\n\n"
        )

        # Write to log file (cross-platform file path)
        with open(log_file_path, "a") as log_file:
            log_file.write(log_entry)

        # Send the log entry via email
        send_email("Daily Bandwidth Usage Log", log_entry, recipient_emails)

        print(f"Bandwidth data logged and emailed:\n{log_entry}")

    except KeyError as e:
        print(f"Missing key in response data: {e}")

# Function to send email
def send_email(subject, body, recipient_emails):
    """
    Sends an email with the specified subject and body to multiple recipients.

    :param subject: Email subject
    :param body: Email body
    :param recipient_emails: List of recipient email addresses
    """
    if not sender_email or not sender_password or not recipient_emails:
        print("Environment variables are not set or are empty.")
        print(f"SMTP_SENDER_EMAIL: {sender_email}")
        print(f"RECIPIENT_EMAILS: {recipient_emails}")
        return

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    try:
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = ", ".join(recipient_emails)
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_emails, msg.as_string())

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

if __name__ == "__main__":
    fetch_bandwidth()
