import alpaca_trade_api as tradeapi

def checkValues(symbol, days, money, ma1, ma2):
    msg = "Error"
    valid = True
    api = tradeapi.REST()
    
    try:
        aapl_asset = api.get_asset(symbol)
        if not(aapl_asset.tradable):
            valid = False
            msg = msg + ", Symbol not found in the Database"
    except:
        valid = False
        msg = msg + ", Symbol not found in the Database"

    if(days < 1):
        valid = False
        msg = msg + ", Incorrect number of Days"
    if(ma1 < 1):
        valid = False
        msg = msg + ", Incorrect number of Moving Average 1"
    if(ma2 < 1):
        valid = False
        msg = msg + ", Incorrect number of Moving Average 2"
    if(ma2 < ma1):
        valid = False
        msg = msg + ", Moving Average 2 must be more larger than Moving Average 1"
    if(money < 1):
        valid = False
        msg = msg + ", Incorrect number of Money"
    if(days < ma2*1.5):
        valid = False
        msg = msg + ", Days must be more larger than Moving Average 2"
    
    return [valid, msg]

def checkValuesBest(days, money, ma1, ma2):
    msg = "Error"
    valid = True
    
    if(days < 1):
        valid = False
        msg = msg + ", Incorrect number of Days"
    if(ma1 < 1):
        valid = False
        msg = msg + ", Incorrect number of Moving Average 1"
    if(ma2 < 1):
        valid = False
        msg = msg + ", Incorrect number of Moving Average 2"
    if(ma2 < ma1):
        valid = False
        msg = msg + ", Moving Average 2 must be more larger than Moving Average 1"
    if(money < 1):
        valid = False
        msg = msg + ", Incorrect number of Money"
    if(days < ma2*1.5):
        valid = False
        msg = msg + ", Days must be more larger than Moving Average 2"
    
    return [valid, msg]