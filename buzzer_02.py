import RPi.GPIO as g
import time

g.setmode(g.BCM)
pin = 25

g.setup(pin, g.OUT)

pwm = g.PWM(pin, 1.0)
pwm.start(50.0)

l = [262, 294, 330, 349, 392, 440, 494, 523]
for a in l:
    time.sleep(0.5)
    pwm.ChangeFrequency(a)

l.reverse()
for a in l:
    time.sleep(0.5)
    pwm.ChangeFrequency(a)


pwm.ChangeDutyCycle(0.0)

pwm.stop()
g.cleanup()
