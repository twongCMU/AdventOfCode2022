
value = {"A":1,
         "B":2,
         "C":3}


win = {"A": "B",
       "B": "C",
       "C": "A",
       }

lose = {"A": "C",
       "B": "A",
       "C": "B",
       }
data = []
with open("input.txt") as f:
    line = f.readlines()

    for l in line:
        v = l.strip()
        if len(v) == 0:
            continue

        (a,b) = v.split(" ")
        data.append((a, b))

score = 0
for (a, b) in data:
    if b == "Y": #draw
        score += value[a]
        score+=3
    elif b == "X": # lose
        score += value[lose[a]]
        score += 0
    else:
        score += value[win[a]]
        score+=6

print(int(score))

