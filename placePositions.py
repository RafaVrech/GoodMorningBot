from configs import *
from datetime import datetime, timezone, timedelta
import pytz
import MetaTrader5 as mt5

def placePositions():
    print("Began placing positions...")

    # Getting 7h candle
    # (-1h because metatrader is in UTC+2)
    data = datetime.utcnow() - timedelta(hours=1)
    candle7 = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_H1, data, 1);

    # Exploding 7h candle info
    (time, open, high, low, close, tick_volume, spread, real_volume) = candle7[0]

    print("... with values:")

    print("________________________________________________________________________________________________________________________")
    print("7h Candle: " + str(candle7))
    print("Actual tick:" + str(mt5.symbol_info_tick("EURUSD")))
    print("________________________________________________________________________________________________________________________")

    # Defining common values
    bt = round(high + triggerOffset, 5)
    tpBuy = round(bt + takeProfit, 5)
    slBuy = round(bt - stopLoss, 5)

    st = round(low - triggerOffset, 5)
    tpSell = round(st - takeProfit, 5)
    slSell = round(st + stopLoss, 5)


    print("Buy Trigger: " + str(bt))
    print("Take Profit BUY: " + str(tpBuy))
    print("Stop Loss BUY: " + str(slBuy))
    print("_____________________________________")
    print("Sell Trigger: " + str(st))
    print("Take Profit SELL: " + str(tpSell))
    print("Stop Loss SELL: " + str(slSell))
 

    print("________________________________________________________________________________________________________________________")

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
        print("resultBuy: " + str(resultBuy))

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
        print("resultSell: " + str(resultSell))
        
    print("...ended placing positions.")
