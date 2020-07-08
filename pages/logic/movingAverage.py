import pandas as pd
import numpy as np
import alpaca_trade_api as tradeapi
from datetime import timezone, datetime, timedelta

def calculate_moving_average_crossovers(symbol, timeframe, nDays, ma1, ma2, money):
    startTime = (datetime.now(timezone.utc) - timedelta(days=nDays)).isoformat()

    stockData = __retrieve_closing_price(symbol, timeframe, startTime)
    
    if (not(stockData['Close Price'].hasnans) and stockData['Close Price'].size > ma2):
        rm1 = stockData['Close Price'].rolling(window=ma1).mean()
        rm2 = stockData['Close Price'].rolling(window=ma2).mean()

        try:
            if rm1[ma2] >= rm2[ma2]:
                action = 'sell'
                signal_detected = __sell()
            else:
                action = 'buy'
                signal_detected = __buy()
        except:
            pass

        auxBuy = []
        auxSell = []
        buyPrice = 0

        for index in range(stockData['Close Price'].size):
            if np.isnan(rm1[index]) or np.isnan(rm2[index]):
                continue
            if auxBuy or action == 'buy':
                if signal_detected(rm1[index], rm2[index]):
                    if action == 'buy':
                        buyPrice = stockData['Close Price'][index]
                        auxBuy.append([stockData['Date'][index], stockData['Close Price'][index]])
                    else:
                        money = money * (stockData['Close Price'][index] / buyPrice)
                        buyPrice = 0
                        auxSell.append([stockData['Date'][index], stockData['Close Price'][index]])
            if rm1[index] >= rm2[index]:
                if not(action == 'sell'):
                    action = 'sell'
                    signal_detected = __sell()
            else:
                if not(action == 'buy'):
                    action = 'buy'
                    signal_detected = __buy()

        if not(auxBuy):
            auxBuy=[[float("NAN"), float("NAN")]]
            action = 'buy'
        if not(auxSell):
            auxSell=[[float("NAN"), float("NAN")]]

        if action == 'sell':
            money = money * (stockData['Close Price'][index] / buyPrice)

        signalsBuyData = pd.DataFrame(data=np.asarray(auxBuy), columns=['Date', 'Price'])
        signalsSellData = pd.DataFrame(data=np.asarray(auxSell), columns=['Date', 'Price'])

        return [stockData, rm1, rm2, signalsBuyData, signalsSellData, money]
    else:
        return [0,0,0,0,0,0]

def __retrieve_closing_price(symbol, timeframe, startTime):
    api = tradeapi.REST()
    barset = api.get_barset(symbol, timeframe, start=startTime)
    aux = []
    for bar in barset[symbol]:
        aux.append([bar.t, bar.c])
    try:
        if not(aux):
            aux = [[float("NAN"), float("NAN")]]
        stockData = pd.DataFrame(data=np.asarray(aux), columns=['Date', 'Close Price'])
        stockData['Close Price'] = pd.to_numeric(stockData['Close Price'], errors='coerce')
    except:
        pass
    
    return stockData

def __sell():
    return lambda left, right: left < right

def __buy():
    return lambda left, right: left >= right