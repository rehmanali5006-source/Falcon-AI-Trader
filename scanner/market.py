import requests

def get_price(symbol):
    # Example: BTCUSDT -> bitcoin
    mapping = {
        "BTCUSDT": "bitcoin",
        "ETHUSDT": "ethereum",
        "BNBUSDT": "binancecoin",
        "SOLUSDT": "solana",
        "XRPUSDT": "ripple",
    }

    coin = mapping.get(symbol.upper())

    if coin is None:
        raise Exception(f"Coin {symbol} not supported yet")

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd"

    r = requests.get(url, timeout=10)
    r.raise_for_status()

    data = r.json()

    return data[coin]["usd"]
