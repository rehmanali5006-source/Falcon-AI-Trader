import requests
import pandas as pd

# CoinGecko Coin IDs
COIN_IDS = {
    "BTCUSDT": "bitcoin",
    "ETHUSDT": "ethereum",
    "BNBUSDT": "binancecoin",
    "SOLUSDT": "solana",
    "XRPUSDT": "ripple"
}


def get_price(symbol):
    coin = COIN_IDS[symbol]

    url = (
        f"https://api.coingecko.com/api/v3/simple/price"
        f"?ids={coin}&vs_currencies=usd"
    )

    r = requests.get(url, timeout=10)
    r.raise_for_status()

    data = r.json()

    return float(data[coin]["usd"])


def get_candles(symbol, interval="1h", limit=200):
    # CoinGecko free API OHLC candles provide nahi karti.
    # Isliye current price se temporary DataFrame banate hain.

    price = get_price(symbol)

    df = pd.DataFrame({
        "time": [pd.Timestamp.now()],
        "open": [price],
        "high": [price],
        "low": [price],
        "close": [price],
        "volume": [0.0]
    })

    return df
