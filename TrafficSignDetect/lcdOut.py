import RPi.GPIO as GPIO
from RPLCD import CharLCD

# Set up the LCD
lcd = CharLCD(cols=16, rows=4, pin_rw=None, pin_rs=37, pin_e=35, 
              pins_data=[33, 31, 29, 40], numbering_mode=GPIO.BOARD)

# Clear the LCD
lcd.clear()

# Function to display text on the LCD
def display_on_lcd(text):
    lcd.clear()
    lcd.write_string(text)



lcd.write_string("Speed: 53kmph")
lcd.cursor_pos = (1, 0)  # Set cursor to second line, first column
lcd.write_string("Limit: 60kmph")

# Move cursor to third line, second column
lcd.cursor_pos = (2, 0)
lcd.write_string("Pedestrain Cross ahead")

# Move cursor to fourth line, third column
# lcd.cursor_pos = (3, 0)
# lcd.write_string("Line 4: LCD")

