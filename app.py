from scanner.market import get_price
from scanner.coins import COINS

print("=" * 40)
print("🚀 Falcon AI Trader")
print("=" * 40)

for coin in COINS:
    try:
        price = get_price(coin)
        print(f"{coin:10} : ${price}")
    except Exception as e:
        print(f"{coin}: ERROR - {e}")
