from collections import defaultdict

sum = 0
with open("input.txt") as f:
    line = f.readlines()
    print(f"lines of data {len(line)}")

    for i in range(0, len(line), 3):

        data = defaultdict(int)
        for j in range(3):
            print(f"line {i}+{j}")            
            v = line[i+j].strip()
            if len(v) == 0:
                break

            # oops, each row can have the same letter multiple times
            # so hack in a dedup
            seen = set()
            for l in v:
                if l in seen:
                    continue
                data[l] += 1
                seen.add(l)


        for k,v in data.items():
            if v != 3:
                continue
            
            if k.isupper():
                sum += ord(k)-38
                print(f"uper letter {k} has value {ord(k)-38}")
            else:
                sum += ord(k)-96
                print(f"lower letter {k} has value {ord(k)-96}")
                

        print(int(sum))



