#from collections import defaultdict
#import sys
#import numpy as np



with open("input.txt") as f:
    line = f.readlines()


reg = 1
clock = 1


count = 0
for l in line:
    v = l.strip()
    if len(v) == 0:
        continue

    if v == "noop":
        clock += 1
    else:
        (_,val) = v.split(" ")
        val = int(val)


        clock += 1
        if clock >= 20 and (clock-20) % 40 == 0:
            count += (clock * reg)

        clock += 1
        reg += val

    
    if clock >= 20 and (clock-20) % 40 == 0:
        count += (clock * reg)

print(f"Part 1 count {count}")
