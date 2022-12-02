
value = {"A":1,
         "B":2,
         "C":3}

win = {"A": "B",
       "B": "C",
       "C": "A",
       }
data = []
with open("input.txt") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue

        (a,b) = v.split(" ")
        if b == "X":
            b = "A"
        if b == "Y":
            b = "B"
        if b == "Z":
            b = "C"
            
        data.append((a, b))

score = 0
for (a, b) in data:
    if a == b:
        score += 3
    elif win[a] == b:
        score += 6

        
    score+=value[b]

print(int(score))

