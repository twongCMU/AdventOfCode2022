from collections import defaultdict
import sys
import numpy as np



with open("input.txt") as f:
    line = f.readlines()


h_x = 0
h_y = 0
t_x = 0
t_y = 0
visited = set()
visited.add((t_x, t_y))

for l in line:
    v = l.strip()
    if len(v) == 0:
        continue

    (dir, dist) = v.split(" ")
    dist = int(dist)


    for i in range(dist):
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

        if h_x - t_x == 2:
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

        print(f"dir {dir} now head {h_x}x{h_y} tail {t_x}x{t_y}")
        visited.add((t_x, t_y))
print(f"part 1 visited {len(visited)}")
print(f"{sorted(visited)}")
