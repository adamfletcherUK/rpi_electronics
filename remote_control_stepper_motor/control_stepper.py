import time
from adafruit_motor import stepper
from remote_control_stepper_motor.controller_info import Controller

class ControlStepper(Controller):
    def __init__(self, keypad_val=None):
        super().__init__()
        self.keypad_val = keypad_val

    def get_stepper_configs(self):
        if self.keypad_val == "A":
            direction = stepper.FORWARD
        if self.keypad_val == "B":
            direction = stepper.BACKWARD

        return direction

    def test_run_stepper_motor(self):
        for i in range(200):
            self.motor_kit.stepper1.onestep(direction=stepper.BACKWARD)
            time.sleep(0.01)

    def run_stepper_motor(self):
        direction = self.get_stepper_configs()
        for i in range(200):
            self.motor_kit.stepper1.onestep(direction=direction)

if __name__ == '__main__':
    ControlStepper().test_run_stepper_motor()
