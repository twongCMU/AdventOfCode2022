from collections import defaultdict
import sys
import numpy as np

items = {0:[73, 77],
         1:[57, 88, 80],
         2:[61, 81, 84, 69, 77, 88],
         3:[78, 89, 71, 60, 81, 84, 87, 75],
         4:[60, 76, 90, 63, 86, 87, 89],
         5:[88],
         6:[84, 98, 78, 85],
         7:[98, 89, 78, 73, 71],
         }
    

# if divisible by a, throw to monkey b, otherwise throw to c
test = [
    (11, 6, 5),
    (19, 6, 0),
    (5, 3, 1),
    (3, 1, 0),
    (13, 2, 7),
    (17, 4, 7),
    (7, 5, 4),
    (2, 3, 2),
]
"""
items = {0:[79, 98],
         1:[54, 65, 75, 74],
         2:[79, 60, 97],
         3:[74],
         }
test = [
    (23, 2, 3),
    (19, 2, 0),
    (13, 1, 3),
    (17, 0, 1),
    ]
"""
counts = [0]*8
for i in range(20):
    print(f"Round {i}")
    # for each monkey
    for m in range(8):
        print(f"Monkey {m}")
        # for each item that monkey has
        while len(items[m]):
            v = items[m].pop(0)
            new_v = v

            # inspect worry level
            counts[m] += 1

            
            if m == 0:
                new_v *= 5
            elif m == 1:
                new_v += 5
            elif m == 2:
                new_v *= 19
            elif m == 3:
                new_v += 7
            elif m == 4:
                new_v += 2
            elif m == 5:
                new_v += 1
            elif m == 6:
                new_v *= new_v
            elif m == 7:
                new_v += 4
            else:
                raise
            """
            if m == 0:
                new_v *= 19
            elif m == 1:
                new_v += 6
            elif m == 2:
                new_v *= new_v
            elif m == 3:
                new_v += 3
            else:
                raise
            """
            # relief
            new_v = int(new_v/3)

            (divisor, true_monkey, false_monkey) = test[m]
            
            if new_v % divisor == 0:
                items[true_monkey].append(new_v)
            else:
                items[false_monkey].append(new_v)

            
            
print(f"{sorted(counts)}")
