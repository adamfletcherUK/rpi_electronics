import RPi.GPIO as IO
from time import time

PIN = 14



def setup(pin):
    # Numbers GPIOs by physical location
    IO.setwarnings(False)
    IO.setmode(IO.BCM)
    IO.setup(pin, IO.IN, pull_up_down=IO.PUD_DOWN)  # GPIO 14 -> IR sensor as input
    #GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location

# # define a function to acquire data
def binary_acquire(pin, duration):
    # acquires data as quickly as possible
    t0 = time() # time is in seconds here
    results = []
    while (time() - t0) < duration:
        results.append(IO.input(pin))
    return results

# if __name__ == '__main__':
#     setup(PIN)
#     print("Acquiring data for 1 second")
#     # acquire data for 1 second
#     results = binary_acquire(PIN, 1.0)
#     print("Done!")
#
#     for i in results:
#         print(i)
#     IO.cleanup()


def on_ir_receive(pinNo, bouncetime=150):
    # when edge detect is called (which requires less CPU than constant
    # data acquisition), we acquire data as quickly as possible
    data = binary_acquire(pinNo, bouncetime/1000.0)
    if len(data) < bouncetime:
        return
    rate = len(data) / (bouncetime / 1000.0)
    pulses = []
    i_break = 0
    # detect run lengths using the acquisition rate to turn the times in to microseconds
    for i in range(1, len(data)):
        if (data[i] != data[i-1]) or (i == len(data)-1):
            pulses.append((data[i-1], int((i-i_break)/rate*1e6)))
            i_break = i
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
        return int(outbin, 2)
    except ValueError:
        # probably an empty code
        return None


def destroy():
    IO.cleanup()


if __name__ == "__main__":
    setup(PIN)
    try:
        print("Starting IR Listener")
        while True:
            print("Waiting for signal")
            IO.wait_for_edge(PIN, IO.FALLING)
            code = on_ir_receive(PIN)
            if code:
                print(str(hex(code)))
            else:
                print("Invalid code")
    except KeyboardInterrupt:
        pass
    except RuntimeError:
        # this gets thrown when control C gets pressed
        # because wait_for_edge doesn't properly pass this on
        pass
    print("Quitting")
    destroy()