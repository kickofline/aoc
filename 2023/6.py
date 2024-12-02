f = open("6.txt", "r")
data = f.read()

times = [int(i) for i in list(filter(lambda x: x.isnumeric(), data.split("\n")[0].split(" ")))]
times2 = [40828492]
distances = [int(i) for i in list(filter(lambda x: x.isnumeric(), data.split("\n")[1].split(" ")))]
distances2 = [233101111101487]

numWays = []
for i in range(len(times)):
    time = times[i]
    goal = distances[i]
    numWays.append(0)
    for hold in range(time):
        distance = (time*hold) - (hold*hold)
        if distance > goal:
            numWays[i] += 1

total = 1
for i in numWays: total = total*i
print(total)


numWays = []
for i in range(len(times2)):
    time = times2[i]
    goal = distances2[i]
    numWays.append(0)
    for hold in range(time):
        distance = (time*hold) - (hold*hold)
        if distance > goal:
            numWays[i] += 1

total = 1
for i in numWays: total = total*i
print(total)