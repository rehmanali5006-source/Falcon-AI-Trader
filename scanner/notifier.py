import requests

NTFY_TOPIC = "crypto-alerts"


def send_notification(message):

    url = f"https://ntfy.sh/{NTFY_TOPIC}"

    response = requests.post(
        url,
        data=message.encode("utf-8"),
        headers={
            "Title": "Falcon AI Trader",
            "Priority": "default"
        },
        timeout=10
    )

    response.raise_for_status()

    print("Notification Sent")
