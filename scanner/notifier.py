import requests

NTFY_TOPIC = "crypto-alerts"


def send_notification(title, message):

    url = f"https://ntfy.sh/{NTFY_TOPIC}"

    headers = {
        "Title": title,
        "Priority": "default",
        "Tags": "chart_with_upwards_trend"
    }

    response = requests.post(
        url,
        data=message.encode("utf-8"),
        headers=headers,
        timeout=15
    )

    response.raise_for_status()

    return True
