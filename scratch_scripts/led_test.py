from gpiozero import LED
from time import sleep

led = LED(17)

def blinker():
    led.on()
    sleep(1)
    led.off()
    sleep(1)

if __name__ == '__main__':
    while True:
        blinker()


