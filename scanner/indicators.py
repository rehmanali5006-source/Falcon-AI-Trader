import pandas as pd


def add_indicators(df):

    # EMA 20
    df["EMA20"] = df["close"].ewm(span=20).mean()

    # EMA 50
    df["EMA50"] = df["close"].ewm(span=50).mean()

    # RSI
    delta = df["close"].diff()

    gain = delta.where(delta > 0, 0).rolling(14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(14).mean()

    rs = gain / loss

    df["RSI"] = 100 - (100 / (1 + rs))

    # MACD
    ema12 = df["close"].ewm(span=12).mean()
    ema26 = df["close"].ewm(span=26).mean()

    df["MACD"] = ema12 - ema26
    df["MACD_SIGNAL"] = df["MACD"].ewm(span=9).mean()

    return df
