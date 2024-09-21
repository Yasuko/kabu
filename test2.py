import yfinance as yf

msft = yf.Ticker("9984.T")

r = msft.info
#r = msft.history(start="2022-12-10", end="2022-12-20", period="1d")

print(r)