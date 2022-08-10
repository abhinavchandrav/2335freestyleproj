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
# Code provided by Professor Rossetti

def to_pct(my_number):
    """
    Formats a decimal number as a percentage, rounded to 4 decimal places, with a percent sign.
    
    Param my_number (float) like 0.95555555555
    
    Returns (str) like '95.5556%'
    """
    return f"{(my_number * 100):.4f}%"

# Set Up - Securely ask for an API key 
# Code provided by Professor Rossetti

from getpass import getpass
api_key = getpass("Please input your AlphaVantage API Key: ")

# -----------------------------------------------------------

from pandas import read_csv
import pandas as pd

# -----------------------------------------------------------

def stock_momentum_report(symbol = "NFLX"):
    t_csv_filepath = f"https://www.alphavantage.co/query?function=TREASURY_YIELD&interval=daily&maturity=1year&apikey={api_key}&datatype=csv"
    t_df = read_csv(t_csv_filepath)
    csv_filepath = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol.upper()}&outputsize=full&apikey={api_key}&datatype=csv"
    df = read_csv(csv_filepath)
    try: 
        latest_close = df.iloc[0]["adjusted_close"]
        # The stock market is open for 252 days in the US - use 251 to pull the data from a year prior on this day
        earliest_close = df.iloc[251]["adjusted_close"]
        print(df["timestamp"][0], "adjusted close price:", to_usd(latest_close))
        print(df["timestamp"][251], "adjusted close price:", to_usd(earliest_close))
        p_change = ((latest_close - earliest_close) / earliest_close) * 100
        print("percent change in", symbol, (p_change))
        #print(t_df)
        #print(len(t_df))
        t_df.replace(".", float("NaN"), inplace=True)
        t_df.dropna(inplace = True) 
        #print(len(t_df))
        t_yield = t_df.iloc[260]["value"]
        print("Treasury yield is", (t_yield))
        #print(type(t_yeild))
        #print(type(p_change))
        if p_change > float(t_yield):
            print(f"{symbol.upper()} has positive momentum.")
            print(f"Recommendation: Invest in {symbol.upper()}")
        else:
            print(f"{symbol.upper()} has negative momentum.")
            print("Recommendation: Invest in Treasury Bills")
    except KeyError:
        print("OPPS! That ticker is not available.  Please check your symbol and try again.")

symbol = input(("Please enter a ticker:"))

stock_momentum_report(symbol)