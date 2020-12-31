import board
import digitalio
import adafruit_character_lcd.character_lcd as character_lcd
import adafruit_blinka.board.raspberrypi.raspi_40pin as rpi

lcd_rs = digitalio.DigitalInOut(rpi.D22)
lcd_en = digitalio.DigitalInOut(rpi.D17)
lcd_d4 = digitalio.DigitalInOut(rpi.D25)
lcd_d5 = digitalio.DigitalInOut(rpi.D24)
lcd_d6 = digitalio.DigitalInOut(rpi.D23)
lcd_d7 = digitalio.DigitalInOut(rpi.D18)
lcd_backlight = digitalio.DigitalInOut(rpi.D13)

lcd_columns = 16
lcd_rows = 2

lcd = character_lcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

lcd.message = "Hello\nCircuitPython"