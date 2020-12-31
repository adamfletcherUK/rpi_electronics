import time
import os
from adafruit_motor import stepper
from remote_control_stepper_motor.controller_info import Controller

class ControlStepper(Controller):
    def __init__(self, keypad_val=None):
        super().__init__()
        self.keypad_val = keypad_val
        if os.environ['DIRECTION'] == 'FORWARD':
            self.direction = stepper.FORWARD
        if os.environ['DIRECTION'] == 'BACKWARD':
            self.direction = stepper.BACKWARD
        self.speed = float(os.environ['SPEED'])

    def get_stepper_configs(self):
        if self.keypad_val == "A":
            self.direction = stepper.FORWARD
            os.environ['DIRECTION'] = 'FORWARD'
        if self.keypad_val == "B":
            self.direction = stepper.BACKWARD
            os.environ['DIRECTION'] = 'BACKWARD'

        if self.keypad_val == '1':
            os.environ['SPEED'] = '0.45'
        if self.keypad_val == '2':
            os.environ['SPEED'] = '0.04'
        if self.keypad_val == '3':
            os.environ['SPEED'] = '0.035'
        if self.keypad_val == '4':
            os.environ['SPEED'] = '0.03'
        if self.keypad_val == '5':
            os.environ['SPEED'] = '0.025'
        if self.keypad_val == '6':
            os.environ['SPEED'] = '0.02'
        if self.keypad_val == '7':
            os.environ['SPEED'] = '0.015'
        if self.keypad_val == '8':
            os.environ['SPEED'] = '0.01'
        if self.keypad_val == '9':
            os.environ['SPEED'] = '0.005'
        if self.keypad_val == '0':
            os.environ['SPEED'] = '0'
        self.speed = float(os.environ['SPEED'])

    def test_run_stepper_motor(self):
        for i in range(200):
            self.motor_kit.stepper1.onestep(direction=stepper.BACKWARD)
            time.sleep(0.01)

    def run_stepper_motor(self):
        self.get_stepper_configs()
        for i in range(200):
            self.motor_kit.stepper1.onestep(direction=self.direction)
            time.sleep(self.speed)

if __name__ == '__main__':
    ControlStepper().test_run_stepper_motor()
