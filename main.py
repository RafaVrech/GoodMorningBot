import pytz
from datetime import datetime, timezone, timedelta
import MetaTrader5 as mt5

numberOfOrders = 5

def doTheStuff():
    # connect to MetaTrader 5
    if not mt5.initialize():
        print("initialize() failed")
        mt5.shutdown()

    timezone = pytz.timezone("Etc/GMT+1")
    data = datetime.utcnow() - timedelta(hours=1)
    candle7 = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_H1, data, 1);

    (time, open, high, low, close, tick_volume, spread, real_volume) = candle7[0]

    bt = round(high + 0.0007, 5)
    st = round(low - 0.0007, 5)
    tpSell = round(st - 0.0005, 5)
    slSell = round(st + 0.0050, 5)
    tpBuy = round(bt + 0.0005, 5)
    slBuy = round(bt - 0.0050, 5)

    for i in range(numberOfOrders):
        symbol = "EURUSD"
        symbol_info = mt5.symbol_info(symbol)
        lot = 0.1
        
        point = mt5.symbol_info(symbol).point
        deviation = 20

        requestBuy = {
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
        }

        requestSell = {
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
        }

        # send a trading request
        resultBuy = mt5.order_send(requestBuy)
        print("resultBuy: " + str(resultBuy))

        resultSell = mt5.order_send(requestSell)
        print("resultSell: " + str(resultSell))

    # shut down connection to MetaTrader 5
    mt5.shutdown()


def doAnotherStuff():
    # connect to MetaTrader 5
    if not mt5.initialize():
        print("initialize() failed")
        mt5.shutdown()

    orders = mt5.orders_get(symbol="EURUSD")

    if(len(orders) == numberOfOrders):
        for ordem in orders:
            request = {
                "action": mt5.TRADE_ACTION_REMOVE,
                "order": ordem.ticket,
                "symbol": "EURUSD"
            }
            
            result = mt5.order_send(request)

            print("result: " + str(result))
        mt5.shutdown()
        exit()

    mt5.shutdown()
