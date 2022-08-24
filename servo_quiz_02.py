import RPi.GPIO as g
import time

g.setmode(g.BCM)
servo = 16

g.setup(servo, g.OUT)
pwm = g.PWM(servo, 50)
pwm.start(12.5)

time.sleep(2.0)
pwm.ChangeDutyCycle(0.0)

pwm.stop()
g.cleanup()
