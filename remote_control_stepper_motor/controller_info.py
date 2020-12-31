import busio
import RPi.GPIO as GPIO
import adafruit_blinka.board.raspberrypi.raspi_40pin as rpi
from adafruit_motorkit import MotorKit

class Controller:
    def __init__(self):
        GPIO.setwarnings(False)
        self.SCL = rpi.SCL
        self.SDA = rpi.SDA
        self.pinMode = GPIO.BCM
        self.motor_kit = MotorKit(i2c=busio.I2C(scl=rpi.SCL,
                                                sda=rpi.SDA))
    def Pinouts(self):
        self.ir_input_pin = 14
        self.L1, self.L2, self.L3, self.L4 = 5, 6, 13, 19
        self.C1, self.C2, self.C3, self.C4 = 12, 16, 20, 21