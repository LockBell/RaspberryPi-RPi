import RPi.GPIO as g
import time

g.setmode(g.BCM)
pin = 25

g.setup(pin, g.OUT)

pwm = g.PWM(pin, 1.0)
pwm.start(50.0)

l = [262, 294, 330]
for i in range(0, 3):
    for a in l:
        time.sleep(0.5)
        pwm.ChangeFrequency(a)

pwm.ChangeDutyCycle(0.0)

pwm.stop()
g.cleanup()
