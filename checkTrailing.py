from configs import *
from datetime import datetime, timezone, timedelta
import pytz
import MetaTrader5 as mt5

def checkTrailing():

    positions = mt5.positions_get(symbol="EURUSD")
    print(positions)
    
    # for position in positions:
    #     if()
    #     if(position.profit >= 5):
    #         resultBuy = mt5.order_send({
    #             "symbol": position.symbol,
    #             "sl": position.price_open + 0.0002,
    #             "tp": position.price_open + 0.0002,
    #             "comment": "python trailing stop",
    #             "action": mt5.TRADE_ACTION_SLTP,
    #             "position": position.ticket,
    #         })

    #         print(resultBuy)
    
    