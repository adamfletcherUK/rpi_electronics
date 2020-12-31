import RPi.GPIO as GPIO
import time
from remote_control_stepper_motor.controller_info import Controller

class KeypadRead(Controller):
    def __init__(self):
        super().__init__()
        super().Pinouts()
        GPIO.setmode(self.pinMode)

    def setupChannels(self):
        for l_pin in [self.L1, self.L2, self.L3, self.L4]:
            GPIO.setup(l_pin, GPIO.OUT)

        for c_pin in [self.C1, self.C2, self.C3, self.C4]:
            GPIO.setup(c_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def readColumn(self, line, characters):
        keypad_val = None
        GPIO.output(line, GPIO.HIGH)
        if GPIO.input(self.C1):
            keypad_val = characters[0]
        if GPIO.input(self.C2):
            keypad_val = characters[1]
        if GPIO.input(self.C3):
            keypad_val = characters[2]
        if GPIO.input(self.C4):
            keypad_val = characters[3]
        GPIO.output(line, GPIO.LOW)

        return keypad_val

    def readRow(self):
        number_val = False
        L1val = self.readColumn(self.L1, ["1", "2", "3", "A"])
        L2val = self.readColumn(self.L2, ["4", "5", "6", "B"])
        L3val = self.readColumn(self.L3, ["7", "8", "9", "C"])
        L4val = self.readColumn(self.L4, ["*", "0", "#", "D"])
        if L1val is not None:
            number_val = L1val
        elif L2val is not None:
            number_val = L2val
        elif L3val is not None:
            number_val = L3val
        elif L4val is not None:
            number_val = L4val

        return number_val


    def run(self):
        self.setupChannels()
        try:
            while True:
                keypad_val = self.readRow()
                if keypad_val:
                    print(f"Keypad Val: {self.readRow()}")

        except KeyboardInterrupt:
            GPIO.cleanup()
            print(f"\nApplication stopped!")


if __name__ == '__main__':
    KeypadRead().run()



