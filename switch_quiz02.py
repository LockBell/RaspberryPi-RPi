import RPi.GPIO as g

btnPre = False
led = False

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
        if b and not btnPre:
            print('rising')
            led = True if not led else False
            g.output(p1, led)
            g.output(p2, led)

        elif not b and btnPre:
            print('fall')

        else:
            pass

        btnPre = b

except KeyboardInterrupt:
    pass

g.cleanup()
