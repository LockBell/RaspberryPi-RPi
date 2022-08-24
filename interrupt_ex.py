import RPi.GPIO as g
g.setmode(g.BCM)

ledS = False
ledC = False

def press(channel):
    global ledS
    global ledC
    ledS = not ledS
    ledC = True

btn = 18
p1 = 23
p2 = 24

g.setup(btn, g.IN)
g.setup(p1, g.OUT)
g.setup(p2, g.OUT)

g.add_event_detect(btn, g.RISING)
g.add_event_callback(btn, press)

try:
    while True:
        if ledC:
            ledC = False
            g.output(p1, ledS)
            g.output(p2, ledS)

except KeyboardInterrupt:
    pass

g.cleanup()
