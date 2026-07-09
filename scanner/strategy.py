from scanner.indicators import add_indicators


def check_signal(df):

    df = add_indicators(df)

    last = df.iloc[-1]

    score = 0
    reasons = []

    # EMA Trend
    if last["EMA20"] > last["EMA50"]:
        score += 40
        reasons.append("EMA Bullish")

    # RSI
    if last["RSI"] < 35:
        score += 30
        reasons.append("RSI Oversold")

    # MACD
    if last["MACD"] > last["MACD_SIGNAL"]:
        score += 30
        reasons.append("MACD Bullish")

    # Final Signal
    if score >= 70:
        signal = "BUY"
    elif score <= 30:
        signal = "SELL"
    else:
        signal = "HOLD"

    return {
        "signal": signal,
        "score": score,
        "reasons": reasons
    }
