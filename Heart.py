import math
from turtle import*
def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 13*math.cos(k)-5*math.cos(2*k)-2*math.cos(3*k)-math.cos(4*k)
speed()
bgcolor('black')
for i in range(6000):
    goto(hearta(i*math.pi/180),heartb(i*math.pi/180))
    for j in range(1):
        color("red")