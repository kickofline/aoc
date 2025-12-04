with open('input', 'r') as f:
    input = f.read()

from collections import defaultdict

def check(x, y, map):
    c = 0
    if map[(x,y)] == False: return False
    ###
    ###
    ###
    if map[(x-1,y+1)]: c += 1
    if map[(x,y+1)]: c += 1
    if map[(x+1,y+1)]: c += 1
    if map[(x-1,y)]: c += 1
    if map[(x+1,y)]: c += 1
    if map[(x-1,y-1)]: c += 1
    if map[(x,y-1)]: c += 1
    if map[(x+1,y-1)]: c += 1
    return c < 4

sum = 0
map = defaultdict(bool)
for y,row in enumerate(input.split("\n")):
    for x,cell in enumerate(row):
        map[(x,y)] = cell == "@"

for y in range(len(input.splitlines())):
    for x in range(len(input.splitlines()[0])):
        if check(x, y, map):
            sum += 1

print(sum)

sum = 0
def removeRolls(map):
    removedMap = {}
    for y in range(len(input.splitlines())):
        for x in range(len(input.splitlines()[0])):
            if check(x, y, map):
                removedMap[(x,y)] = True
        #         print("x", end="")
        #     else:
        #         print("@" if map[(x,y)] else ".", end="")
        # print()
    if (len(removedMap) == 0):
        return 0
    else:
        for k in removedMap: map[k] = False
        return len(removedMap) + removeRolls(map)

print(removeRolls(map))