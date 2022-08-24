import RPi.GPIO as g
import time

g.setmode(g.BCM)

pin1 = 23
pin2 = 24

g.setup(pin1, g.OUT)
g.setup(pin2, g.OUT)

try:
    while True:
        g.output(pin1, True)
        g.output(pin2, True)
        time.sleep(0.001)
        g.output(pin1, False)
        g.output(pin2, False)
        time.sleep(0.009)
except KeyboardInterrupt:
    pass

g.cleanup()
