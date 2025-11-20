import yfinance as yf

def get_live_price(ticker: str):
    data = yf.Ticker(ticker)
    return data.history(period="1d")['Close'][-1]

def get_intraday_data(ticker: str, interval="5m"):
    data = yf.Ticker(ticker)
    return data.history(period="1d", interval=interval)
