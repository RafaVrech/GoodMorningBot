
def checkRemove():
    
    orders = mt5.orders_get(symbol="EURUSD")

    if(len(orders) == positionsMultiplier):
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