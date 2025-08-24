import os
import requests
import time

# Webhook is stored securely in Render environment variable
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# 🔥 Your message goes here 🔥
MESSAGE = "@everyone Join now! 🎮 https://rbx-url.com/W-UggYLz"

# Send every 1 minute (60 seconds)
INTERVAL_SECONDS = 60

def send_webhook():
    if not WEBHOOK_URL:
        print("❌ ERROR: DISCORD_WEBHOOK_URL not set in environment!")
        return
    payload = {
        "content": MESSAGE,
        "allowed_mentions": {"parse": ["everyone"]}
    }
    r = requests.post(WEBHOOK_URL, json=payload, timeout=10)
    print("Status:", r.status_code, "| Response:", r.text)

if __name__ == "__main__":
    while True:
        send_webhook()
        time.sleep(INTERVAL_SECONDS)
