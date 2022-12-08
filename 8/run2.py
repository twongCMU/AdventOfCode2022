from collections import defaultdict
import sys
import numpy as np



with open("input.txt") as f:
    line = f.readlines()

w=len(line[0])-1
h=len(line)

data = np.zeros((w, h), dtype = np.int8)
print(f"Size is {h}x{w}")
def check(x, y, dx, dy):
    orig_value = data[x][y]
    x+=dx
    y+=dy

    distance = 0
    # don't go off the edge
    while x >= 0 and y >= 0 and x < w and y < h:
        distance+=1
        # if the tree is taller than the original it is blocked so we're done
        if data[x][y] >= orig_value:
            return distance

        x+=dx
        y+=dy


        
    # we didn't find a blocking tree so we are visible
    return distance

    
for x, l in enumerate(line):
    v = l.strip()
    if len(v) == 0:
        continue

    for y, v in enumerate(v):
       data[x][y] = v

print(f"{data}")
max_score = 0
for x in range(w):
    for y in range(h):
        a = check(x,y,0,-1)
        b = check(x,y,-1,0)
        c = check(x,y,0,1)
        d = check(x,y,1,0)
        score = a*b*c*d
        print(f"{x}x{y}: {a} {b} {c} {d} {score}")
        if score > max_score:
            max_score = score

print(f"part 2 max score {max_score}")



