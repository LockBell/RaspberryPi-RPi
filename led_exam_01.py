import RPi.GPIO as g
import time

g.setmode(g.BCM);
pin1 = 23
pin2 = 24

g.setup(pin1, g.OUT)
g.setup(pin2, g.OUT)

g.output(pin1, True)
g.output(pin2, True)

time.sleep(2.0)

g.output(pin1, False)
g.output(pin2, False)

g.cleanup()
