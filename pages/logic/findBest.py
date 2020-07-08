import alpaca_trade_api as tradeapi
import random

from .movingAverage import calculate_moving_average_crossovers

def findBest(timeframe, nDays, ma1, ma2, money):
    api = tradeapi.REST()
    active_assets = api.list_assets(status='active')
    nasdaq_assets = [a.symbol for a in active_assets if a.exchange == 'NASDAQ']

    dataBest = [["", [0,0,0,0,0,0]], ["", [0,0,0,0,0,0]]]
    
    for symbol in nasdaq_assets:
        data = calculate_moving_average_crossovers(symbol, timeframe, nDays, ma1, ma2, money)
        if dataBest[0][1][5] < data[5]:
            dataBest[1] = dataBest[0]
            dataBest[0] = [symbol, data]
        elif dataBest[1][1][5] < data[5]:
            dataBest[1] = [symbol, data]
    
    return dataBest