from scanner.coins import COINS
from scanner.market import get_candles
from scanner.strategy import check_signal


def scan_market():

    print("=" * 50)
    print(" Falcon AI Trader Scanner ")
    print("=" * 50)

    for coin in COINS:

        try:

            df = get_candles(coin)

            current_price = df.iloc[-1]["close"]

            signal = check_signal(df)

            print(f"Coin   : {coin}")
            print(f"Price  : {current_price}")
            print(f"Signal : {signal}")
            print("-" * 50)

        except Exception as e:

            print(f"{coin} ERROR : {e}")


if __name__ == "__main__":
    scan_market()
