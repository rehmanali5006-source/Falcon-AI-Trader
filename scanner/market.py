from binance.client import Client

client = Client()

def get_client():
    return client


def get_price(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker["price"])


if __name__ == "__main__":
    print(get_price("BTCUSDT"))
