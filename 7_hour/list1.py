import random
epiclist = ["e", "p", "i", "k", ":O"]
print(epiclist)
print(len(epiclist))
print(epiclist[len(epiclist)-1])
print(epiclist[-len(epiclist)+1])

badlist = epiclist
badlist.pop(2)
badlist.append(random.randint(1,6))

if 5 in badlist:
    print("KK")
else:
    pass

fun = random.randint(0,4)
print(badlist)
badlist.insert(3, epiclist[fun])
print(badlist)