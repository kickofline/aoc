from collections import defaultdict
from functools import cmp_to_key

D = open("7.txt", "r").read().strip()
Lines = D.split('\n')
card_order_dict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10,"J":11, "Q":12, "K":13, "A":14}

hands = [l.split(" ")[0] for l in Lines]
bids = [l.split(" ")[1] for l in Lines]

def rankHand(h):
    value_counts = defaultdict(lambda:0)
    for v in h: value_counts[v]+=1
    sort = (sorted(value_counts.values()))
    if not h:
        return 0
    match sort:
        case [5]: 
            return 7
        case [1,4]:
            return 6
        case [2,3]:
            return 5
        case [1,1,3]:
            return 4
        case [1,2,2]:
            return 3
        case [1,1,1,2]:
            return 2 
        case [1,1,1,1,1]:
            return 1
        case _:
            return 0

def compareHands(first, second): 
    # true for first is better, false if second is better

    if rankHand(first) > rankHand(second) or (first and not second):
        return 1
    elif rankHand(first) < rankHand(second) or (second and not first):
        return -1
    else:
        
        for i in range(5):
            print(card_order_dict[first[i]])


print(sorted(hands, key=cmp_to_key(compareHands)))

