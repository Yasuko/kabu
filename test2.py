import yfinance as yf

msft = yf.Ticker("9984.T")

r = msft.info

print(r)