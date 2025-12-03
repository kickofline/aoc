with open('input', 'r') as f:
    input = f.read()

sum = 0
for idRange in input.split(","):
    r =idRange.split("-")
    for id in range(int(r[0]),int(r[1])+1):
        if(str(id)[:len(str(id))//2] == str(id)[len(str(id))//2:]):
            sum += id
print(sum)

#part 2

import re

sum = 0
for idRange in input.split(","):
    r =idRange.split("-")
    for id in range(int(r[0]),int(r[1])+1):          
        if(re.match(r"(\d+)\1+$",str(id))):
            sum += id
print(sum)
