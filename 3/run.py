

sum = 0
with open("input.txt") as f:
    line = f.readlines()


    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue
        data=set()
       
        half = int(len(v)/2)
        a = v[:half]
        b = v[half:]

        for l in a:
            data.add(l)

        for l in b:
            if l in data:
                if l.isupper():
                    sum += ord(l)-38
                    print(f"uper letter {l} has value {ord(l)-38}")
                else:
                    sum += ord(l)-96
                    print(f"lower letter {l} has value {ord(l)-96}")

                break
print(int(sum))



