from scanner.coins import COINS
from scanner.market import get_candles
from scanner.strategy import check_signal
from scanner.notifier import send_notification


def main():

    print("=" * 60)
    print("🚀 Falcon AI Trader")
    print("=" * 60)

    for coin in COINS:

        try:

            df = get_candles(coin)

            result = check_signal(df)

            price = df.iloc[-1]["close"]

            print(f"\nCoin       : {coin}")
            print(f"Price      : {price:.4f}")
            print(f"Signal     : {result['signal']}")
            print(f"Confidence : {result['score']}%")

            if result["reasons"]:
                print("Reasons:")
                for reason in result["reasons"]:
                    print(f"  ✔ {reason}")

            print("-" * 60)

            if result["signal"] in ["BUY", "SELL"]:

                message = (
                    f"{result['signal']} SIGNAL\n\n"
                    f"Coin: {coin}\n"
                    f"Price: {price:.4f}\n"
                    f"Confidence: {result['score']}%\n\n"
                    f"Reasons:\n"
                )

                for reason in result["reasons"]:
                    message += f"• {reason}\n"

                send_notification(
                    f"{coin} {result['signal']}",
                    message
                )

        except Exception as e:

            print(f"{coin} ERROR : {e}")


if __name__ == "__main__":
    main()
