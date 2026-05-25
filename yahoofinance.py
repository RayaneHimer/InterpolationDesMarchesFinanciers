import yfinance as yf

print("Running")

ticker = 'AAPL'
start_date = '2025-01-01'
end_date = '2026-05-01'


data = yf.download(ticker, start=start_date, end=end_date)


data.to_csv(f'{ticker}_historical_data.csv')
