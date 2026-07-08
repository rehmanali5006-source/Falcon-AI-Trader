import pandas as pd


def check_signal(df):
    """
    Returns:
        BUY / SELL / HOLD
    """

    if len(df) < 60:
        return "HOLD"

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

    if (
        last["EMA20"] > last["EMA50"]
        and last["RSI"] < 35
    ):
        return "BUY"

    elif (
        last["EMA20"] < last["EMA50"]
        and last["RSI"] > 65
    ):
        return "SELL"

    return "HOLD"
