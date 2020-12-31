"""Simple test for using adafruit_motorkit with a stepper motor"""
import time
import board
from adafruit_motorkit import MotorKit
import busio
import adafruit_blinka.board.raspberrypi.raspi_40pin as rpi
from adafruit_motor import stepper

kit = MotorKit(i2c= busio.I2C(scl=rpi.SCL, sda=rpi.SDA))

print("running stepper motor")

for i in range(200):
    #200 == full revolution
    kit.stepper1.onestep(direction=stepper.BACKWARD)
    time.sleep(0.01)

