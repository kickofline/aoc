with open('input', 'r') as f:
    input = f.read()

# sum = 0
# for bank in input.split("\n"):
#     largest = 0
#     for b in range(len(bank)):
#         for b2 in range(b+1,len(bank)):
#             newLargest = int(bank[b] + bank[b2])
#             largest = max(largest, newLargest)
#     sum += largest

# print(sum)

# import itertools


def batteryOfSize(bank, n):
    bigBattery = ""
    for i in range(n-1,-1,-1):
        allowedRange = bank[:-i] if i != 0 else bank # bank[:0] gives empty list
        bigBattery = bigBattery + max(allowedRange)
        bank = bank[bank.index(bigBattery[-1])+1:]
    return(int(bigBattery))
    
sum1 = sum2 = 0
for bank in input.split("\n"):
    sum1 += batteryOfSize(bank, 2)
    sum2 += batteryOfSize(bank, 12)

print(sum1)
print(sum2)