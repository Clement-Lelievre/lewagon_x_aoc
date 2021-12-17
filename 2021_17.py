area = 'target area: x=81..129, y=-150..-108'

# Find the initial velocity that causes the probe to reach the highest y position 
# and still eventually be within the target area after any step. 
# What is the highest y position it reaches on this trajectory?

# The probe's x,y position starts at 0,0. Then, it will follow some trajectory by moving in steps. On each step, these changes occur in the following order:

# The probe's x position increases by its x velocity.
# The probe's y position increases by its y velocity.
# Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
# Due to gravity, the probe's y velocity decreases by 1.

X = range(81,130)
Y = range(-150, -107)
# X = range(20,31)
# Y = range(-10, -4)


def launch(x:int, y:int) -> int | None:
    position = [0,0]
    y_history = []
    while True:
        position[0] += x
        position[1] += y
        y_history.append(position[1])
        if (position[0] in X) and (position[1] in Y):
            return max(y_history)
        if x > 0:
            x -= 1
        elif x < 0:
            x += 1 
        y -= 1
        if position[0] > X[-1] or position[1] < Y[0]:
            break
      
# x = 15
# pos = 0
# print(f'step 0: 0')
# step = 1
# while x >= 0:
#     pos += x
#     print(f'step {step}: x = {pos}')

#     x -= 1
#     step += 1

# x = 15 is the optimal x because this way, at some point we'll be in free fall for x = 120, so falling straight down into the area
from tqdm import tqdm

# c = 0
# for x in tqdm(range(130)):
#     for y in range(1500):
#         if (a:= launch(x,y)) is not None:
#             c += 1
# print(c)

x = 20
pos = 0
while x >= 0:
    pos += x
    x -= 1
    print(pos)

        
# strat: partir très haut puis tomber à pic (quand x=0) sur l'abscisse x = 130
# pour cela, je dois déterminer le x initial

# from collections import defaultdict
# d = defaultdict(int)

# for start_x in range(5,131):
#     d[start_x] = 0
#     pos = 0
#     x = start_x
#     steps = 0
#     while x > 0 and pos < 131:
#         pos += x
#         x -= 1
#         steps += 1
#     if x == 0:
        
# x = 0
# while True:
#     print(x, x*(x-1)/2)
#     x += 1
#     if x*(x-1)/2 > 130:
#         break

# x = 15
# steps = 0
# pos = 0
# while True:
#     pos += x
#     x -= 1
#     steps += 1
#     print(f'step n° {steps}: pos = {pos}')
#     if x == 0:
#         break

# part 2
