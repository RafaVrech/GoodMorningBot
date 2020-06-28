import MetaTrader5 as mt5
from configs import *

def checkRemove():
    # print("Began checking remove...")

    orders = mt5.orders_get(symbol="EURUSD")

    if(len(orders) == positionsMultiplier):
        print("Removing positions left")
        for ordem in orders:
            request = {
                "action": mt5.TRADE_ACTION_REMOVE,
                "order": ordem.ticket,
                "symbol": "EURUSD"
            }
            
            result = mt5.order_send(request)

            print("result: " + str(result))
        # exit()

    # print("...ended checking remove.")