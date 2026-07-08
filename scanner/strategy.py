import pandas as pd


def check_signal(df):

    if len(df) < 60:
        return {
            "signal": "HOLD",
            "confidence": 0
        }

    # EMA
    df["EMA20"] = df["close"].ewm(span=20).mean()
    df["EMA50"] = df["close"].ewm(span=50).mean()

    # RSI
    delta = df["close"].diff()

    gain = delta.where(delta > 0, 0).rolling(14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(14).mean()

    rs = gain / loss
    df["RSI"] = 100 - (100 / (1 + rs))

    last = df.iloc[-1]

    confidence = 5

    if last["EMA20"] > last["EMA50"]:
        confidence += 2

    if last["RSI"] < 35:
        confidence += 2

    if confidence > 10:
        confidence = 10

    if last["EMA20"] > last["EMA50"] and last["RSI"] < 35:
        signal = "BUY"

    elif last["EMA20"] < last["EMA50"] and last["RSI"] > 65:
        signal = "SELL"

    else:
        signal = "HOLD"

    return {
        "signal": signal,
        "confidence": confidence
    }
