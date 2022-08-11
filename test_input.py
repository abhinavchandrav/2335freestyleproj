# This tests the user input which in turn tests the API 
# A data point that comes in through the API is part of the input_stock function

from run import input_stock

def test_input():
    assert input_stock('NFLX') == "Valid"
    assert input_stock('XYABC') == "The ticker you have entered is not a valid ticker.  Please check your ticker and try again."