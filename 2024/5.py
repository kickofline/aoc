with open('./5.txt', 'r') as f:
    input = f.read()
    
p1 = 0
p2 = 0

rules = [tuple(i.split("|")) for i in input.split('\n\n')[0].splitlines()]
updates = input.split('\n\n')[1].splitlines()

from functools import cmp_to_key

def compare_pages(X, Y):
    for rule in rules:
        if rule == (X, Y): 
            return -1
        if rule == (Y, X):
            return 1
    return 0


for update in updates:
    pages = update.split(',')
    for (x,y) in rules:
        if x in pages and y in pages and pages.index(x) > pages.index(y): break
    else: # valid
        p1 += int(pages[len(pages)//2])
        continue
    # invalid
    fixed = sorted(pages, key=cmp_to_key(compare_pages))
    p2 += int(fixed[len(fixed)//2])
    
print(p1)
print(p2)