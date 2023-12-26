import turtle as t
from random import random

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         color(c)
#         forward(steps)
#         right(30)

# while True:
#     forward(200)
#     left(170)
#     right(40)
#     if abs(pos()) < 1:
#         break
    
for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)