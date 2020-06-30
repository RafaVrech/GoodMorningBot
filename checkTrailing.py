from configs import *
from datetime import datetime, timezone, timedelta
import pytz
import MetaTrader5 as mt5
import copy 
 
def checkTrailing():

    stepRatio = 2
    stepValue = (takeProfit / stepRatio) * pip 

    positions = mt5.positions_get(symbol=symbol)
    
    for position in positions:

        if(position.type == mt5.ORDER_TYPE_BUY):

            # When almost hit profit target
            if(position.price_current >= position.tp - 2 * pip):

                print("\nBUY position triggered trailing ----------------------------------------\n")

                # Safety measure
                # if(position.sl != position.price_open):
                #     stepValue = position.sl - position.price_open

                resultBuy = mt5.order_send({
                    "symbol": position.symbol,
                    "sl": position.sl + stepValue,
                    "tp": position.tp + stepValue,
                    "comment": "python trailing stop",
                    "action": mt5.TRADE_ACTION_SLTP,
                    "position": position.ticket,
                })

        elif(position.type == mt5.ORDER_TYPE_SELL):
            # When almost hit profit target
            if(position.price_current <= position.tp - 2 * pip):

                print("\nSELL position triggered trailing ----------------------------------------\n")

                # Safety measure
                # if(position.sl != position.price_open):
                #     stepValue = position.price_open - position.sl

                resultBuy = mt5.order_send({
                    "symbol": position.symbol,
                    "sl": position.sl - stepValue,
                    "tp": position.tp - stepValue,
                    "comment": "python trailing stop",
                    "action": mt5.TRADE_ACTION_SLTP,
                    "position": position.ticket,
                })

                print(resultBuy)
    