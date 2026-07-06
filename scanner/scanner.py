from scanner.coins import COINS
from scanner.market import get_price
from config import CONFIDENCE_THRESHOLD


def calculate_score(price):
    score = 0

    if price > 0:
        score += 20

    return score


def scan_market():
    print("=" * 50)
    print(" Falcon AI Trader Scanner ")
    print("=" * 50)

    for coin in COINS:
        try:
            price = get_price(coin)
            score = calculate_score(price)

            print(f"{coin} | Price: {price} | Score: {score}")

            if score >= CONFIDENCE_THRESHOLD:
                print(">>> TRADE FOUND <<<")

        except Exception as e:
            print(f"{coin} ERROR : {e}")


if __name__ == "__main__":
    scan_market()
