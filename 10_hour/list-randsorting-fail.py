import random

originlist = list(range(1,11))
newlist = [1]
steps = 0

while True:
    for i in range(0,len(originlist)):
        num = originlist[random.randint(0,9)]
        for i in range(0, len(newlist)):
            if num == newlist[i]:
                num = originlist[random.randint(0,9)]
                print(f"does {num} = {newlist[i]}")
            else:
                newlist.append(num)
                steps += 1
    newlist.pop(0)
    break

print(newlist)
print(steps)