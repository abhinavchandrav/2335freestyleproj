# Set Up - USD formatting 
# Code provided by Professor Rossetti

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    
    Param: my_price (int or float) like 4000.444444
    
    Example: to_usd(4000.444444)
    
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" 

# Set Up - Percent formatting 
# Initial code provided by Professor Rossetti - small changes made 

def to_pct(my_number):
    """
    Formats a decimal number as a percentage, rounded to 4 decimal places, with a percent sign.
    
    Param my_number (float) like 0.95555555555
    
    Returns (str) like '95.5556%'
    """
    return f"{(my_number):.2f}%"

# -----------------------------------------------------------

from pandas import read_csv
import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv()

# -----------------------------------------------------------

def stock_momentum_report(df, t_df, symbol = "NFLX"):
    print("--------------------------------------------")

    latest_close = df.iloc[0]["adjusted_close"]
    # The stock market is open for 252 days in the US
    # Use 251 to pull the data from a year prior 
    earliest_close = df.iloc[251]["adjusted_close"]
    print(df["timestamp"][0], "adjusted close price:", to_usd(latest_close))
    print(df["timestamp"][251], "adjusted close price:", to_usd(earliest_close))
    
    p_change = ((latest_close - earliest_close) / earliest_close) * 100
    print(f"Percent change in {symbol}: {to_pct(p_change)}")

    print("--------------------------------------------")
    
    t_df.replace(".", float("NaN"), inplace=True)
    t_df.dropna(inplace = True) 

    # Treasury yield data is published 260 days of the year to account for weekends and holidays 
    # Use 259 to pull the data from a year prior
    t_yield = t_df.iloc[259]["value"]
    print(t_df["timestamp"][259], f"Treasury yield is: {t_yield}%")

    print("--------------------------------------------")

    if p_change > float(t_yield):
        print(f"{symbol.upper()} has POSITIVE momentum.")
        print(f"Recommendation: Invest in {symbol.upper()}")
    else:
        print(f"{symbol.upper()} has NEGATIVE momentum.")
        print("Recommendation: Invest in Treasury Bills")
    
    print("--------------------------------------------")
