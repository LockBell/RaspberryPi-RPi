import RPi.GPIO as g
import time

g.setmode(g.BCM)
pin1 = 23
pin2 = 24

g.setup(pin1, g.OUT)
g.setup(pin2, g.OUT)

try:
    while True:
        for i in range(0, 11):
            g.output(pin1, True)
            g.output(pin2, True)
            time.sleep(i*0.001)
            g.output(pin1, False)
            g.output(pin1, False)
            time.sleep((10-i) * 0.001)

        for i in range(10, -1, -1):
            g.output(pin1, True)
            g.output(pin2, True)
            time.sleep(i * 0.001)
            g.output(pin1, False)
            g.output(pin2, False)
            time.sleep((10-i) * 0.001)

except KeyboardInterrupt:
    pass
g.cleanup()
