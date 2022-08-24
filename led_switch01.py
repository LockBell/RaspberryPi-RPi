import RPi.GPIO as g

g.setmode(g.BCM)

bpin = 18
g.setup(bpin, g.IN)

try:
    while True:
        binput = g.input(bpin)
        print(binput)
except KeyboardInterrupt:
    pass

g.cleanup()

