from collections import defaultdict
import sys

count = 0
count2 = 0

"""
            [C]         [N] [R]    
[J] [T]     [H]         [P] [L]    
[F] [S] [T] [B]         [M] [D]    
[C] [L] [J] [Z] [S]     [L] [B]    
[N] [Q] [G] [J] [J]     [F] [F] [R]
[D] [V] [B] [L] [B] [Q] [D] [M] [T]
[B] [Z] [Z] [T] [V] [S] [V] [S] [D]
[W] [P] [P] [D] [G] [P] [B] [P] [V]
 1   2   3   4   5   6   7   8   9 
"""
data = {
    1:'WBDNCFJ',
    2:'PZVQLST',
    3:'PZBGJT',
    4:'DTLJZBHC',
    5:'GVBJS',
    6:'PSQ',
    7:'BVDFLMPN',
    8:'PSMFBDLR',
    9:'VDTR',
}


for k in data.keys():
    data[k] = list(data[k])

with open("input.txt") as f:
    line = f.readlines()


    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        
        (d_move, d_from, d_to) = v.split(" ")
        d_move = int(d_move)
        d_from = int(d_from)
        d_to = int(d_to)
        
        for i in range(d_move):
            one_value = data[d_from].pop()
            data[d_to].append(one_value)

for k in sorted(data.keys()):
    sys.stdout.write(data[k][-1])

print(" ")
