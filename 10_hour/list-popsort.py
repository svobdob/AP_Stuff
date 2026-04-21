import random

originlist = list(range(0, 33))
newlist = []

print(originlist)

for i in range(len(originlist)):
    num = random.randint(0, len(originlist)-1)
    newlist.append(originlist[num])
    originlist.pop(num)

print(newlist)