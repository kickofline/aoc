with open('./2.txt', 'r') as f:
    input = f.read()

def safe(ll):
    return (
            (
                all(i < j for i,j in zip(ll, ll[1:])) or  # decreasing
                all(i > j for i,j in zip(ll, ll[1:]))     # increasing 
            ) and 
            all(abs(i-j) > 0 and abs(i-j) < 4 for i,j in zip(ll, ll[1:]))) # acceptable diff

numSafe = 0
for level in input.split("\n"):
    ll = list(map(int, level.split()))
    
    if safe(ll):
        numSafe += 1
        continue

    for i in range(len(ll)):
        modified_levels = ll[:i] + ll[i+1:]
        if safe(modified_levels):
            numSafe += 1
            break


print(numSafe)