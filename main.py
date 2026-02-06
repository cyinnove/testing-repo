# demo_api_usage.py
import requests
import os

# --- BEST PRACTICE: Load sensitive credentials from environment variables ---
API_KEY = <redacted>
API_SECRET = <redacted>

if not API_KEY or not API_SECRET:
    raise ValueError("API credentials not set in environment variables!")

# --- Example API request using credentials ---
url = "https://api.example.com/data"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "X-Secret": API_SECRET
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Success! Data:", response.json())
else:
    print("Error:", response.status_code, response.text)
