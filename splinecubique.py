import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy.interpolate import CubicSpline

print("Analyse...")

df = pd.read_csv('AAPL_historical_data.csv', skiprows=2, header=0)
df.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
df = df.sort_values('Date').reset_index(drop=True)

df['Close_smooth'] = df['Close'].rolling(window=10).mean()
df = df.dropna()

dates = df['Date']
prices = df['Close_smooth'].values
dates_num = mdates.date2num(dates)

# Spline cubique
cs = CubicSpline(dates_num, prices)

# Extrapolation
last_date = dates_num[-1]
future_dates_num = np.linspace(last_date, last_date + 3, 3)
future_prices = cs(future_dates_num)
future_dates = mdates.num2date(future_dates_num)

# Graphe
plt.figure(figsize=(12, 6))
plt.plot(dates, prices, label='Données historiques (lissées)', color='blue')
plt.plot(future_dates, future_prices, label='Extrapolation (3 jours)',
         color='red', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Prix de clôture (USD)')
plt.title('Extrapolation du prix AAPL par spline cubique')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('aapl_spline_extrapolation.png', dpi=150, bbox_inches='tight')
plt.show()