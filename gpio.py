import RPi.GPIO as g

g.setmode(g.BCM)
btn1, btn2 = 14, 15
led1, led2, led3, led4 = 18, 23, 24, 25
g.setup(btn1, g.IN)
g.setup(btn2, g.IN)
g.setup(led1, g.OUT)
g.setup(led2, g.OUT)
g.setup(led3, g.OUT)
g.setup(led4, g.OUT)

try:
    while True:
        bt = g.input(btn1)
        g.output(led1, bt)
        g.output(led2, bt)
        b1 = g.input(btn2)
        g.output(led3, b1)
        g.output(led4, b1)
except KeyboardInterrupt:
    g.cleanup()

