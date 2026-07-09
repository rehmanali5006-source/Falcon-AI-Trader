import requests
import pandas as pd

BASE_URL = "https://api.binance.com/api/v3/klines"


def get_candles(symbol, interval="1h", limit=200):

    # BTCUSDT same rahega
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()

    candles = response.json()

    df = pd.DataFrame(
        candles,
        columns=[
            "time",
            "open",
            "high",
            "low",
            "close",
            "volume",
            "close_time",
            "quote_volume",
            "trades",
            "taker_buy_base",
            "taker_buy_quote",
            "ignore"
        ]
    )

    df = df[[
        "time",
        "open",
        "high",
        "low",
        "close",
        "volume"
    ]]

    numeric = [
        "open",
        "high",
        "low",
        "close",
        "volume"
    ]

    for col in numeric:
        df[col] = df[col].astype(float)

    df["time"] = pd.to_datetime(df["time"], unit="ms")

    return df


def get_price(symbol):
    df = get_candles(symbol, limit=1)
    return float(df.iloc[-1]["close"])
