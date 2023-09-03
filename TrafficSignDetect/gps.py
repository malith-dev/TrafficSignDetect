import serial              
from time import sleep
import sys
import pynmea2
import lcdOut

ser = serial.Serial ("/dev/ttyS0", boudrate=9600, timeout=1)
try:
    while True:
        received_data = (str)(ser.readline()) #read NMEA string received
        print(received_data, "\n")
        lcdOut.display_on_lcd(received_data)
except KeyboardInterrupt:
    sys.exit(0)  


def speedTrack():
    while True:
    try:
        # Read a line of data from the GPS module
        data = ser.readline().decode('utf-8')
        
        # Check if the line starts with '$GPRMC' (or '$GPVTG' if you prefer)
        if data.startswith('$GPRMC'):
            msg = pynmea2.parse(data)
            
            # Extract the speed in knots
            speed_knots = msg.spd_over_grnd
            
            # Convert to other units if needed (e.g., km/h)
            speed_kmh = speed_knots * 1.852
            
            print(f"Speed (knots): {speed_knots}")
            print(f"Speed (km/h): {speed_kmh}")
    
    except KeyboardInterrupt:
        # Exit the loop when you press Ctrl+C
        break

# Close the serial port when done
ser.close()
