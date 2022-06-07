"""Simple test for using adafruit_motorkit with a DC motor"""
import busio
import time
import board
import adafruit_blinka.board.raspberrypi.raspi_40pin as rpi
from adafruit_motorkit import MotorKit

print(f"SLC= {rpi.SCL}")
print(f"SDA= {rpi.SDA}")

busio.I2C(scl=rpi.SCL, sda=rpi.SDA)
kit = MotorKit(i2c= busio.I2C(scl=rpi.SCL, sda=rpi.SDA))

kit.motor1.throttle = 1.0
time.sleep(0.5)
kit.motor1.throttle = 0

