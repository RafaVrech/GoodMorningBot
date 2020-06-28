import atexit
import schedule
import time
from checkRemove import checkRemove
from checkTrailing import checkTrailing
from placePositions import placePositions
from mt5API import stop, start

### INIT ###

@atexit.register
def stopMT5():
    stop()

start()



### SCHEDULES ###

# schedule.every(1).day.at("08:01").do(placePositions)
# placePositions()
# schedule.every(5).seconds.do(checkRemove)
schedule.every(5).seconds.do(checkTrailing)


### LOOP ###

while True:
    schedule.run_pending()
    time.sleep(1)
