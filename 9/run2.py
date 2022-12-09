from collections import defaultdict
import sys
import numpy as np



with open("input.txt") as f:
    line = f.readlines()


knots = []
for i in range(10):
    knots.append((0,0))

visited = set()
visited.add((0,0))

for l in line:
    v = l.strip()
    if len(v) == 0:
        continue

    (dir, dist) = v.split(" ")
    dist = int(dist)


    for iteration in range(dist): # head moves
        print(f"{dir} {iteration}")
        (h_x, h_y) = knots[0]
        if dir == "U":
            h_y += 1
        elif dir == "D":
            h_y -= 1
        elif dir == "R":
            h_x += 1
        elif dir == "L":
            h_x -= 1
        else:
            assert(f"unexpected direction {dir}")

        knots[0] = (h_x, h_y)
        
        for i in range(9): # knots updates, last 10th knot doesn't affect any subsequent ones
            (h_x, h_y) = knots[i]
            (t_x, t_y) = knots[i+1]

            # first 4 cases are when it is diagonal 2 away
            # move next knot 1 diagonal
            # remaining 4 cases are same as before
            if h_x - t_x == 2 and h_y - t_y == 2:
                t_x += 1
                t_y += 1
            elif h_x - t_x == -2 and h_y - t_y == -2:
                t_x -= 1
                t_y -= 1
            elif h_y - t_y == 2 and h_x - t_x == -2:
                t_y += 1
                t_x -=1
            elif h_y - t_y == -2 and h_x - t_x == 2:
                t_y -= 1
                t_x +=1  
            elif h_x - t_x == 2:
                # head is 2 right of tail, move tail right
                t_x += 1
                t_y = h_y
            elif h_x - t_x == -2:
                # head is 2 left of tail, move tail left
                t_x -= 1
                t_y = h_y
            elif h_y - t_y == 2:
                # head is 2 above tail, move tail up
                t_y += 1
                t_x = h_x
            elif h_y - t_y == -2:
                # head is 2 below tail, move tail down
                t_y -= 1
                t_x = h_x

            knots[i+1] = (t_x, t_y)

        print(f"{knots}")
        visited.add(knots[-1])
print(f"part 2 visited {len(visited)}")
#print(f"{sorted(knots)}")
