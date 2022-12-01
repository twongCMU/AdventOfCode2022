

data = []
with open("input.txt") as f:
    local_sum = 0
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            data.append(local_sum)
            local_sum = 0
            continue
        
        local_sum += int(v)

print(max(data))

# part 2
data.sort()
print(data[-1]+data[-2]+data[-3])
