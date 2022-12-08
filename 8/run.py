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

    # don't go off the edge
    while x >= 0 and y >= 0 and x < w and y < h:

        # if the tree is taller than the original it is blocked so we're done
        if data[x][y] >= orig_value:
            return False

        x+=dx
        y+=dy

    # we didn't find a blocking tree so we are visible
    return True

    
for x, l in enumerate(line):
    v = l.strip()
    if len(v) == 0:
        continue

    for y, v in enumerate(v):
       data[x][y] = v

print(f"{data}")
visible = 0
for x in range(w):
    for y in range(h):
        if check(x,y,1,0) or check(x,y,-1,0) or check(x,y,0,1) or check(x,y,0,-1):
            visible += 1

print(f"part 1 visible {visible}")



