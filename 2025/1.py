with open('input', 'r') as f:
    input = f.read()


dial = 50
sum = 0

for i in input.split("\n"):
    if i[0] == "L":
        dial -= int(i[1:])
    else:
        dial += int(i[1:])
    if dial % 100 == 0: sum += 1
    

print(sum)


dial = 50
sum = 0

for i in input.split("\n"):
    r = int(i[1:])
    print(i)
    for _ in range(r):
        if i[0] == "L":
            dial -= 1
        else:
            dial += 1
        dial %= 100
        if dial == 0: sum += 1
    print("sum: " + str(sum))
    print("dial: " + str(dial))
print(sum)

