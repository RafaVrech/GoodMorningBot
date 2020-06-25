import atexit
import schedule
import time
from checkRemove import checkRemove
from placePositions import placePositions
from mt5API import stop, start

### INIT ###

@atexit.register
def stopMT5():
    stop()

start()



### SCHEDULES ###

schedule.every(1).day.at("08:01").do(placePositions)
schedule.every(30).seconds.do(checkRemove)



### LOOP ###

while True:
    schedule.run_pending()
    time.sleep(1)
