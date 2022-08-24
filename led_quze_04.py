import RPi.GPIO as g
import time

g.setmode(g.BCM)

pin1 = 23
pin2 = 24

g.setup(pin1, g.OUT)
g.setup(pin2, g.OUT)

pwm1 = g.PWM(pin1, 1000.0)
pwm1.start(0.0)
pwm2 = g.PWM(pin2, 1000.0)
pwm2.start(0.0)

try:
    while True:
        for i in range(0, 101):
            pwm1.ChangeDutyCycle(i)
            pwm2.ChangeDutyCycle(i)
            time.sleep(0.01)
        for i in range(100, -1, -1):
            pwm1.ChangeDutyCycle(i)
            pwm2.ChangeDutyCycle(i)
            time.sleep(0.01)
        
except KeyboardInterrupt:
    pass

pwm1.stop()
pwm2.stop()

g.cleanup()
