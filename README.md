# 📊 Bandwidth Monitor & Email Logger

This Python script fetches daily bandwidth usage from a remote JSON API, converts values to gigabytes, appends the result to a local log file, and optionally emails the usage report to one or more recipients.

---

## 🔧 Features

- 🌐 Fetches bandwidth data from a configurable API endpoint
- 📈 Converts raw byte values to human-readable GB format
- 🗂 Appends logs to a local file `bandwidth_log.txt` (cross-platform compatible)
- 📬 Sends daily bandwidth logs via email using Gmail SMTP
- 🔒 All configuration handled via environment variables

---

## 📁 Project Structure

1. bandwidth_logger.py # Main script 
1. bandwidth_log.txt # Output log file (auto-created) .
1. env (optional) # Use for local testing with dotenv

---

## 📦 Environment Variables

Set the following environment variables before running the script:

| Variable           | Description                                |
|--------------------|--------------------------------------------|
| `JMS_URL`          | The API URL to fetch bandwidth data        |
| `SENDER_EMAIL`     | Gmail sender email                         |
| `SENDER_PASSWORD`  | Gmail app-specific password                |
| `RECIPIENT_EMAILS` | Comma-separated list of recipient emails   |

Example (Linux/macOS):
```bash
export JMS_URL=https://your-server.com/api
export SENDER_EMAIL=your_email@gmail.com
export SENDER_PASSWORD=your_app_password
export RECIPIENT_EMAILS=alice@example.com,bob@example.com
```

## Sample Output
```
2025-04-25 10:00:00 - Bandwidth Data (in GB):
  Monthly Limit: 1000.00 GB
  Used: 284.25 GB
  Reset Day: 1
```

## 🚀 How to Run
```bash
python bandwidth_logger.py


```

## Notes
For Gmail, you may need to use an app-specific password and enable "Less secure apps" (or OAuth in production).

The script is designed to be platform-independent (Windows/Linux/macOS).