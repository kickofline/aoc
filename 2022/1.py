f = open("1.txt", "r")
splitCals = f.read().split('\n\n')

elfCals = []

for i in splitCals:
    count = 0
    for j in i.split("\n"):
        count += int(j)
    elfCals.append(count)
elfCals.sort()
print(elfCals)
print(elfCals[-1] + elfCals[-2] + elfCals[-3])