import os
from gps import *
from time import *
import threading

gpsd = None  # seting the global variable

class GpsPoller(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global gpsd  # bring it in scope
        gpsd = gps(mode=WATCH_ENABLE)  # starting the stream of info
        self.current_value = None
        self.running = True  # setting the thread running to true

    def run(self):
        global gpsd
        while gpsp.running:
            gpsd.next()  # this will continue to loop and grab EACH set of gpsd info to clear the buffer

if __name__ == '__main__':
    gpsp = GpsPoller()  # create the thread
    try:
        gpsp.start()  # start it up
        while True:
            os.system('clear')
            print('GPS reading')
            print('----------------------------------------')
            print('latitude    ' , gpsd.fix.latitude)
            print('longitude   ' , gpsd.fix.longitude)
            print('speed (m/s) ' , gpsd.fix.speed)
            print('----------------------------------------')
            sleep(1)  # wait a little bit between each poll
    except (KeyboardInterrupt, SystemExit):  # when you press ctrl+c
        print("\nStopping GPS program...")
        gpsp.running = False
        gpsp.join()  # wait for the thread to finish what it's doing
