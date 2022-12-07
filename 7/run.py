from collections import defaultdict
import sys

# This did not go well x.x

# a dict of every directory and 0 file size and file with each file size
filesystem = defaultdict(int)
with open("input.txt") as f:
    line = f.readlines()

cur_dir = ["/"]

filesystem_consumed = 0
for l in line:
    v = l.strip()
    if len(v) == 0:
        continue
      
    if v[0] == '$':
        commands = v.split(' ')

        # $ ls
        # $ cd foobar
        if commands[1] == "ls":
            continue
        elif commands[1] == "cd" and commands[2] == "/":
            cur_dir = ["/"]
        elif commands[1] == "cd" and commands[2] != "..":
            cur_dir.append(commands[2])
            continue
        elif commands[1] == "cd" and commands[2] == "..":
            cur_dir.pop()
        else:
            assert(f"unknown command {v}")
    else:
        info = v.split(' ')
        if info[0] == "dir":
            cur_dir_str = '/'.join(cur_dir)
            cur_dir_str+=f"/{info[1]}/"
            filesystem[cur_dir_str] = 0
            continue
        else:
            filesize = int(info[0])
            filename = info[1]

            cur_dir_str = '/'.join(cur_dir)
            cur_dir_str+=f"/{filename}"
            if cur_dir_str not in filesystem:
                filesystem[cur_dir_str] = filesize
                filesystem_consumed += filesize

print(f"{filesystem}")


part_2_free = 70000000
part_2_best_diff = 70000000
to_free= 30000000-(70000000-filesystem_consumed) # part 2

total_sum = 0
# for every directory (ending with /) look for all of the files under it and sum their sizes
# then see if it is a candidate for deletion
for k1 in filesystem.keys():
    if k1[-1] != '/':
        continue
    dir_sum = 0
    for k2 in filesystem.keys():
        if k2.startswith(k1):
            dir_sum += filesystem[k2]
    if dir_sum <= 100000:
        total_sum += dir_sum

    print(f"{k1}: {dir_sum}")

    if dir_sum > to_free:
        this_part2_diff = dir_sum - to_free
        if this_part2_diff < part_2_best_diff:
            part_2_best_diff = this_part2_diff
            part_2_free = dir_sum
        
print(f"Part 1 {total_sum}")


print(f"Part 2 filesystem size 70000000, consumed {filesystem_consumed}, need to free {to_free}")
print(f"Part 2 {part_2_free}")
