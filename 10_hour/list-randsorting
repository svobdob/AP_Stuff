import random

originlist = list(range(1,33))
newlist = []
steps = 0

for i in range((len(originlist))):
    while True:
        num = random.randint(0, len(originlist)-1)
        steps += 1
        if originlist[num] != None:
            newlist.append(originlist[num])
            originlist[num] = None
            break
        else:
            pass

print(newlist)
print(steps)