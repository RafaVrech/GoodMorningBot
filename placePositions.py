from configs import *
from datetime import datetime, timezone, timedelta
import pytz
import MetaTrader5 as mt5

def placePositions():

    # Getting 7h candle
    # (-1h because metatrader is in UTC+2)
    data = datetime.utcnow() - timedelta(hours=1)
    candle7 = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_H1, data, 1);

    # Exploding 7h candle info
    (time, open, high, low, close, tick_volume, spread, real_volume) = candle7[0]

    # Defining common values
    bt = round(high + triggerOffset, 5)
    st = round(low - triggerOffset, 5)
    tpSell = round(st - takeProfit, 5)
    slSell = round(st + stopLoss, 5)
    tpBuy = round(bt + takeProfit, 5)
    slBuy = round(bt - stopLoss, 5)

    # Placing positions
    for i in range(positionsMultiplier):
        symbol = "EURUSD"
        lot = 0.1
        deviation = 20

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
