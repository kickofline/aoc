with open('./4.txt', 'r') as f:
    input = f.read()
    
from collections import defaultdict

# use a defaultdict so we can access invalid keys without python exploding
grid = defaultdict(str)

height = len(input.splitlines())
width = len(input.splitlines()[0])

for y in range(height):
    for x in range(width):
        grid[(x,y)] = input.splitlines()[y][x]
        
count = 0
for y in range(height):
    for x in range(width):
        if grid[(x,y)] == "X":
            # there's got to be a better way to do this
            if (grid[(x+1,y)] + grid[(x+2,y)] + grid[(x+3,y)]) == "MAS": 
                count += 1
            if (grid[(x-1,y)] + grid[(x-2,y)] + grid[(x-3,y)]) == "MAS":
                count += 1
            if (grid[(x,y+1)] + grid[(x,y+2)] + grid[(x,y+3)]) == "MAS":
                count += 1
            if (grid[(x,y-1)] + grid[(x,y-2)] + grid[(x,y-3)]) == "MAS":
                count += 1
            if (grid[(x+1,y+1)] + grid[(x+2,y+2)] + grid[(x+3,y+3)]) == "MAS":
                count += 1
            if (grid[(x-1,y+1)] + grid[(x-2,y+2)] + grid[(x-3,y+3)]) == "MAS":
                count += 1
            if (grid[(x+1,y-1)] + grid[(x+2,y-2)] + grid[(x+3,y-3)]) == "MAS":
                count += 1
            if (grid[(x-1,y-1)] + grid[(x-2,y-2)] + grid[(x-3,y-3)]) == "MAS":
                count += 1
          
                
print(count)

# just kidding duh its an X-MAS puzzle

count2 = 0
for y in range(height):
    for x in range(width):
        if grid[(x,y)] == "A":
            masX = (grid[(x-1,y+1)] + grid[(x+1,y-1)] + grid[(x+1,y+1)] + grid[(x-1,y-1)]) #top left, bottom right, top right, bottom left 
            if (
                 (masX) == "SMSM" or
                 (masX) == "MSSM" or
                 (masX) == "MSMS" or
                 (masX) == "SMMS"
             ):
                count2 += 1
print(count2)