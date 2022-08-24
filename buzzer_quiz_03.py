import RPi.GPIO as g
import time

buzzer = 25

g.setmode(g.BCM)
g.setup(buzzer, g.OUT)

pwm = g.PWM(buzzer, 262)
pwm.start(50.0)

school = [391, 391, 440, 440, 391, 391, 329.63, 329.63,
        391, 391, 329.63, 329.63, 293.66, 293.66, 293.66, 0, 
        391, 391, 440, 440, 391, 391, 329.63, 329.63, 
        391, 329.63, 293.66, 329.63, 261.63, 261.63, 0]

for s in school:
    pwm.ChangeFrequency(s)
    time.sleep(0.5)

pwm.ChangeDutyCycle(0.0)
pwm.stop()
pwm.cleanup()
