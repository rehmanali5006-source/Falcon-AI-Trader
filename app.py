from scanner.market import get_price
from scanner.coins import COINS
import requests

# Apna ntfy topic
NTFY_TOPIC = "crypto-alerts"

print("=" * 50)
print("🚀 Falcon AI Trader")
print("=" * 50)

message = "🚀 Falcon AI Trader\n\n"

for coin in COINS:
    try:
        price = get_price(coin)

        print(f"{coin:10} : ${price}")

        message += f"{coin}: ${price}\n"

    except Exception as e:
        print(f"{coin}: ERROR - {e}")
        message += f"{coin}: ERROR\n"

try:
    requests.post(
        f"https://ntfy.sh/{NTFY_TOPIC}",
        data=message.encode("utf-8"),
        headers={
            "Title": "Falcon AI Trader",
            "Priority": "3"
        },
        timeout=10
    )

    print("\n✅ Notification Sent")

except Exception as e:
    print("\n❌ Notification Failed:", e)
