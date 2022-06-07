import RPi.GPIO as IO
import time
import board
from adafruit_motorkit import MotorKit
import busio
import adafruit_blinka.board.raspberrypi.raspi_40pin as rpi
from adafruit_motor import stepper

kit = MotorKit(i2c= busio.I2C(scl=rpi.SCL, sda=rpi.SDA))


IO.setwarnings(False)
IO.setmode (IO.BCM)
IO.setup(14,IO.IN) #GPIO 14 -> IR sensor as input

while True:
    if(IO.input(14)==False): #object is far away
        for i in range(200):
            # 200 == full revolution
            kit.stepper1.onestep(direction=stepper.BACKWARD)
            time.sleep(0.01)