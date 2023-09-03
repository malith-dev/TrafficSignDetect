#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi
import time
import Adafruit_CharLCD as LCD
import sys

# Raspberry Pi pin setup
lcd_rs = 26
lcd_en = 19
lcd_d4 = 13
lcd_d5 = 6
lcd_d6 = 5
lcd_d7 = 21
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 4

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)


# text = raw_input("Type Something to be displayed: ")
# lcd.message(text)
# Wait 5 seconds
# time.sleep(3.0)
# lcd.clear()


def lcdOut(msg):
    lcd.clear()
    lcd.message(msg)
    time.sleep(5)
    lcd.clear()

    
