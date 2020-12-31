import RPi.GPIO as IO
from time import time
from remote_control_stepper_motor.controller_info import Controller

class ReadIR(Controller):
    def __init__(self):
        super().__init__()

    def setup(self, pin):
        # Numbers GPIOs by physical location
        IO.setwarnings(False)
        IO.setmode(IO.BCM)
        IO.setup(pin, IO.IN, pull_up_down=IO.PUD_DOWN)  # GPIO 14 -> IR sensor as input

    def binary_acquire(self, pin, duration):
        # acquires data as quickly as possible
        t0 = time()  # time is in seconds here
        results = []
        while (time() - t0) < duration:
            results.append(IO.input(pin))
        return results

    def on_ir_receive(self, pinNo, bouncetime=150):
        # when edge detect is called (which requires less CPU than constant
        # data acquisition), we acquire data as quickly as possible
        data = self.binary_acquire(pinNo, bouncetime / 1000.0)
        if len(data) < bouncetime:
            return
        rate = len(data) / (bouncetime / 1000.0)
        pulses = []
        i_break = 0
        # detect run lengths using the acquisition rate to turn the times in to microseconds
        for i in range(1, len(data)):
            if (data[i] != data[i - 1]) or (i == len(data) - 1):
                pulses.append((data[i - 1], int((i - i_break) / rate * 1e6)))
                i_break = i
        #print(pulses)
        # decode ( < 1 ms "1" pulse is a 1, > 1 ms "1" pulse is a 1, longer than 2 ms pulse is something else)
        # does not decode channel, which may be a piece of the information after the long 1 pulse in the middle
        outbin = ""
        for val, us in pulses:
            if val != 1:
                continue
            if outbin and us > 2000:
                break
            elif us < 1000:
                outbin += "0"
            elif 1000 < us < 2000:
                outbin += "1"
        try:
            ir_recieved_val =  int(outbin, 2)
        except ValueError:
            # probably an empty code
            ir_recieved_val = None

        return ir_recieved_val

    def destroy(self):
        IO.cleanup()

    def run(self):
        self.setup(self.ir_input_pin)
        try:
            print("Starting IR Listener")
            while True:
                print("Waiting for signal")
                IO.wait_for_edge(self.ir_input_pin, IO.FALLING)
                code = self.on_ir_receive(self.ir_input_pin)
                print(f"Binary IR Code: {code}")
                if code:
                    print(f"Hex IR Code: {str(hex(code))}")
                else:
                    print("Invalid code")

        except KeyboardInterrupt or RuntimeError:
            pass
        print("qutting")
        self.destroy()




if __name__ == "__main__":
    ReadIR().run()