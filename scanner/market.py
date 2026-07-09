import requests
import pandas as pd

BASE_URL = "https://api.bybit.com/v5/market/kline"


def get_candles(symbol, interval="60", limit=200):

    params = {
        "category": "linear",
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    headers = {
        "User-Agent": "FalconAITrader/1.0"
    }

    response = requests.get(
        BASE_URL,
        params=params,
        headers=headers,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    if data["retCode"] != 0:
        raise Exception(data["retMsg"])

    candles = list(reversed(data["result"]["list"]))

    df = pd.DataFrame(candles, columns=[
        "time",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "turnover"
    ])

    for col in ["open", "high", "low", "close", "volume", "turnover"]:
        df[col] = df[col].astype(float)

    df["time"] = pd.to_datetime(df["time"].astype(int), unit="ms")

    return df


def get_price(symbol):
    df = get_candles(symbol, limit=1)
    return float(df.iloc[-1]["close"])
