import RPi.GPIO as g
import random as rand

g.setmode(g.BCM)

#각 핀 값 저장
btn1, btn2 = 14, 15
led1, led2, led3, led4 = 18, 23, 24, 25

#led 상태 저장하는 변수
s1, s2, s3, s4 = False, False, False, False

g.setup(btn1, g.IN)
g.setup(btn2, g.IN)
g.setup(led1, g.OUT)
g.setup(led2, g.OUT)
g.setup(led3, g.OUT)
g.setup(led4, g.OUT)


