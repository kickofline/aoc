with open('./6.txt', 'r') as f:
    input = f.read()
    
p1 = 0
p2 = 0

from collections import defaultdict

grid = defaultdict(str)

height = len(input.splitlines())
width = len(input.splitlines()[0])

for y in range(height):
    for x in range(width):
        grid[(x,y)] = input.splitlines()[y][x]

direction = 0 # 0 is up, 1 is right, 2 is down, 3 is left

guardXY = [k for k, v in grid.items() if v == "^"][0]

while grid[guardXY]:
    grid[guardXY] = "X"
    if direction == 0: 
        nextXY = (guardXY[0], guardXY[1] - 1)
    if direction == 1:
        nextXY = (guardXY[0] + 1, guardXY[1])
    if direction == 2:
        nextXY = (guardXY[0], guardXY[1] + 1)
    if direction == 3:
        nextXY = (guardXY[0] - 1, guardXY[1])
    if grid[nextXY] == "#":
        direction = (direction + 1) % 4
    else:
        guardXY = nextXY
    # print(guardXY)
    # for y in range(height):
    #     for x in range(width):
    #         print(grid[x,y], end="")
    #     print()
    
print(list(grid.values()).count("X"))