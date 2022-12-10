#from collections import defaultdict
#import sys
#import numpy as np



with open("input.txt") as f:
    line = f.readlines()


reg = 1
clock = 1


row = ["."]*41

for l in line:
    v = l.strip()
    if len(v) == 0:
        continue

   
    #print(f"Start of cycle {clock}, reg is {reg}")
    
    if v == "noop":
         #print(f"Cycle {clock} reg {reg}")
        row_offset = (clock-1) % 40
        if row_offset == reg-1 or row_offset == reg or row_offset == reg+1:
            #print(f"Draw in {row_offset}")
            row[row_offset] = "#"
        if row_offset == 39:
            print(f"{row}")
            row = ["."]*41
        #print(f"End of cycle {clock}, reg is {reg}")
        clock += 1
    else:
        (_,val) = v.split(" ")
        val = int(val)

        
        row_offset = (clock-1) % 40
        #print(f"Cycle {clock} reg {reg}")
        if row_offset == reg-1 or row_offset == reg or row_offset == reg+1:
            #print(f"Draw in {row_offset}")
            row[row_offset] = "#"
        if row_offset == 39:
            print(f"{row}")
            row = ["."]*41
        #print(f"End of cycle {clock}, reg is {reg}")
        clock += 1
        
        #print(f"Start of cycle {clock}, reg is {reg}")
        row_offset = (clock-1) % 40
        #print(f"Cycle {clock} reg {reg}")
        if row_offset == reg-1 or row_offset == reg or row_offset == reg+1:
            #print(f"Draw in {row_offset}")
            row[row_offset] = "#"
        if row_offset == 39:
            print(f"{row}")
            row = ["."]*41

        reg += val
        #print(f"End of cycle {clock}, reg is {reg}")
        clock += 1

