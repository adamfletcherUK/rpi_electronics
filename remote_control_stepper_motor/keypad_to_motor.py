import time
import os
from remote_control_stepper_motor.controller_info import Controller
from remote_control_stepper_motor.control_stepper import ControlStepper
from remote_control_stepper_motor.keypad_read import KeypadRead

class KeypadToMotor(Controller):
    def __init__(self):
        super().__init__()
        super().Pinouts()
        self.input_keypad = KeypadRead()



    def run(self):
        self.input_keypad.setupChannels()
        os.environ['DIRECTION'] = 'FORWARD'
        os.environ['SPEED'] = '0.01'
        try:
            while True:
                keypad_val = self.input_keypad.readRow()

                if keypad_val:
                    print(keypad_val)
                    self.stepper_motor = ControlStepper(keypad_val)
                    self.stepper_motor.run_stepper_motor()

        except KeyboardInterrupt:
            print(f"\nApplication stopped!")

if __name__ == '__main__':
    KeypadToMotor().run()