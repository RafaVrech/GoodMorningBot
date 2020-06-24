import schedule
import time
from main import *

def placeOrders():
    doTheStuff()

def checkOrders():
    doAnotherStuff()

schedule.every(1).day.at("04:01").do(placeOrders)
schedule.every(30).seconds.do(checkOrders)

while True:
    schedule.run_pending()
    time.sleep(1)
