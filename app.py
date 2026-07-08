from scanner.market import get_price

print("=" * 40)
print("🦅 Falcon AI Trader")
print("=" * 40)

price = get_price("BTCUSDT")

print(f"BTC Price : {price}")
