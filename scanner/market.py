import requests

BASE_URL = "https://api.bybit.com/v5/market/kline"

def get_candles(symbol, interval="60", limit=200):
    params = {
        "category": "linear",
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    if data["retCode"] != 0:
        raise Exception(data["retMsg"])

    return data["result"]["list"]
