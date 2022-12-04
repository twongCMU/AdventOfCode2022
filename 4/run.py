from collections import defaultdict

count = 0
count2 = 0
with open("input.txt") as f:
    line = f.readlines()


    for l in line:
        data = set()
        v = l.strip()
        if len(v) == 0:
            continue
        

        (a, b) = v.split(',')

        (a1, a2) = a.split('-')
        (b1, b2) = b.split('-')

        a1 = int(a1)
        a2 = int(a2)
        b1 = int(b1)
        b2 = int(b2)

        # Swap the ranges so that a is always the smaller one
        if a2-a1 > b2-b1:
            temp1 = b1
            temp2 = b2
            b1 = a1
            b2 = a2
            a1 = temp1
            a2 = temp2

        for v in range(b1, b2+1):
            data.add(v)

        all_in = True
        for v in range(a1, a2+1):
            if v not in data:
                all_in = False
                break
        if all_in:
            count+=1

        # part 2
        for v in range(a1, a2+1):
            if v in data:
                count2+=1
                break
print(f"Part 1 {count}")
print(f"Part 2 {count2}")
        
