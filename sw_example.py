import RPi.GPIO as g

g.setmode(g.BCM)

btn = 18
led1 = 23
led2 = 24

g.setup(btn, g.IN)
g.setup(led1, g.OUT)
g.setup(led2, g.OUT)

try:
    while True:
        btnInput = g.input(btn)
        g.output(led1, btnInput)
        g.output(led2, btnInput)
except KeyboardInterrupt:
    pass
g.cleanup()
