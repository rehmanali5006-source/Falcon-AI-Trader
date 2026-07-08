from scanner.coins import COINS
from scanner.market import get_candles
from scanner.strategy import check_signal
import pandas as pd


def scan_market():

    print("=" * 60)
    print(" Falcon AI Trader ")
    print("=" * 60)

    for coin in COINS:

        try:

            candles = get_candles(coin)

            close_prices = [float(c[4]) for c in reversed(candles)]

            df = pd.DataFrame({
                "close": close_prices
            })

            current_price = df.iloc[-1]["close"]

            result = check_signal(df)

            print(f"\nCoin       : {coin}")
            print(f"Price      : {current_price:.4f}")
            print(f"Signal     : {result['signal']}")
            print(f"Confidence : {result['score']}%")

            if result["reasons"]:
                print("Reasons:")
                for reason in result["reasons"]:
                    print(f"  ✔ {reason}")

            print("-" * 60)

        except Exception as e:
            print(f"{coin} ERROR : {e}")


if __name__ == "__main__":
    scan_market()
