from momentum import stock_momentum_report

import os
from dotenv import load_dotenv
load_dotenv()

from pandas import read_csv
import pandas as pd

def input_stock(symbol):
    api_key = os.getenv("api_key")
    t_csv_filepath = f"https://www.alphavantage.co/query?function=TREASURY_YIELD&interval=daily&maturity=1year&apikey={api_key}&datatype=csv"
    t_df = read_csv(t_csv_filepath)
    csv_filepath = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol.upper()}&outputsize=full&apikey={api_key}&datatype=csv"
    df = read_csv(csv_filepath)
    try:
        latest_close = df.iloc[0]["adjusted_close"]
        stock_momentum_report(df,t_df,symbol)

    except KeyError:
        print("OPPS! That ticker is not available.  Please check your symbol and try again.")
        return "OPPS! That ticker is not available.  Please check your symbol and try again."
    return "Valid"
