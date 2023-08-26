import yfinance as yf
import pandas as pd
from pandas_datareader import data as pdr 
import datetime as dt
import numpy as np

end_date = dt.datetime.now()

start_date = end_date - dt.timedelta(365*5)

stocks = ['MSFT', 'AAPL', 'TSLA', 'VTI', 'SPY']

df = yf.download(stocks, start=start_date, end=end_date)

df.head()

