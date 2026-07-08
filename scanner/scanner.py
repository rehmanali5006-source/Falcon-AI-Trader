from scanner.coins import COINS
from scanner.market import get_price
from scanner.strategy import check_signal
import pandas as pd


def scan_market():

    print("=" * 50)
    print(" Falcon AI Trader Scanner ")
    print("=" * 50)

    for coin in COINS:

        try:

            price = get_price(coin)

            # Dummy candles (temporary)
            df = pd.DataFrame({
                "close": [price] * 60
            })

            signal = check_signal(df)

            print(f"{coin}")
            print(f"Price : {price}")
            print(f"Signal : {signal}")
            print("-" * 40)

        except Exception as e:
            print(f"{coin} ERROR : {e}")


if __name__ == "__main__":
    scan_market()
