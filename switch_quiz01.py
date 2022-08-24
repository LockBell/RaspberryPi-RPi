import RPi.GPIO as g

g.setmode(g.BCM)

btn = 18
p1 = 23
p2 = 24

g.setup(btn, g.IN)
g.setup(p1, g.OUT)
g.setup(p2, g.OUT)

try:
    while True:
        b = g.input(btn)
        g.output(p1, b)
        g.output(p2, b)

except KeyboardInterrupt:
    pass

g.cleanup()
