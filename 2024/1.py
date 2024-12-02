with open('./1.txt', 'r') as f:
    input = f.read()
    
left = []
right = []

for i in input.split('\n'):
    i = i.split("   ")
    left.append(int(i[0]))
    right.append(int(i[1]))
    
left.sort()
right.sort()

# 1

print(sum(abs(l-r) for (l,r) in zip(left, right)))

# 2

print(sum((right.count(l) * l) for l in left))