from configs import *
from datetime import datetime, timezone, timedelta
import pytz
import MetaTrader5 as mt5

def placePositions():
    print("\nBegan placing positions at BRAZIL time: " + str(datetime.utcnow() - timedelta(hours=3)) + " ...")

    # Getting 7h candle
    # (-1h because metatrader is in UTC+2)
    data = datetime.utcnow() + timedelta(hours=3)
    # candle7 = mt5.copy_rates_from(symbol, mt5.TIMEFRAME_H1, data, 1)
    candle7 = mt5.copy_rates_from(symbol, mt5.TIMEFRAME_M1, datetime.now() + timedelta(hours=3), 1)

    # Exploding 7h candle info
    (time, open, high, low, close, tick_volume, spread, real_volume) = candle7[0]


    print("\n________________________________________________________________________________________________________________________\n")
    print("Opening Candle:")
    print("Time:\t\t\t" + str(datetime.utcfromtimestamp(time)))
    print("Open:\t\t\t" + str(open))
    print("high:\t\t\t" + str(high))
    print("low:\t\t\t" + str(low))
    print("close:\t\t\t" + str(close))


    print("\n________________________________________________________________________________________________________________________\n")

    # Defining common values
    bt = round(high + triggerOffset, 5)
    tpBuy = round(bt + takeProfit, 5)
    slBuy = round(bt - stopLoss, 5)

    st = round(low - triggerOffset, 5)
    tpSell = round(st - takeProfit, 5)
    slSell = round(st + stopLoss, 5)


    print("Buy Trigger:\t\t" + str(bt))
    print("Take Profit BUY:\t" + str(tpBuy))
    print("Stop Loss BUY:\t\t" + str(slBuy))
    print("")
    print("Sell Trigger:\t\t" + str(st))
    print("Take Profit SELL:\t" + str(tpSell))
    print("Stop Loss SELL:\t\t" + str(slSell))
 

    print("\n________________________________________________________________________________________________________________________\n")

    # Placing positions
    for i in range(positionsMultiplier):

        # Place buy position
        resultBuy = mt5.order_send({
            "action": mt5.TRADE_ACTION_PENDING,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_BUY_STOP,
            "price": bt,
            "sl": slBuy,
            "tp": tpBuy,
            "deviation": deviation,
            "comment": "python BUY TIGGER",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_FOK,
        })
        print("\nPlaced BUY:\n" + str(resultBuy))

        # Place sell position
        resultSell = mt5.order_send({
            "action": mt5.TRADE_ACTION_PENDING,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_SELL_STOP,
            "price": st,
            "sl": slSell,
            "tp": tpSell,
            "deviation": deviation,
            "comment": "python SELL TIGGER",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_FOK,
        })
        print("\nPlaced SELL:\n" + str(resultSell))
        
    print("\n...ended placing positions.\n")
