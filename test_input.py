from run import input_stock

def test_input():
    assert input_stock('NFLX') == "Valid"
    assert input_stock('XYABC') == "OPPS! That ticker is not available.  Please check your symbol and try again."