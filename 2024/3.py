with open('./3.txt', 'r') as f:
    input = f.read()

import re

# 1

total = 0
for m in re.findall("mul\(\d+,\d+\)", input):
    muls = [int(i) for i in re.findall("\d+", m)]
    total += muls[0] * muls[1]
    
print(total)

# 2

total = 0
f = True
for m in re.findall("mul\(\d+,\d+\)|do\(\)|don\'t\(\)", input): # technically against the rules
    if m == "do()":
        f = True
    elif m == "don't()":
        f = False
    else:
        if f:
            muls = [int(i) for i in re.findall("\d+", m)]
            total += muls[0] * muls[1]
    
print(total)

