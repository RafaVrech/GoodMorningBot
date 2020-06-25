import MetaTrader5 as mt5

def stop():
    print("Exiting gracefully...")
    mt5.shutdown()

def start():
    # connect to MetaTrader 5
    if not mt5.initialize():
        print("initialize() failed")
        mt5.shutdown()