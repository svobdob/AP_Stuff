import random

oldlist = []
size = int(input("Zadejte velikost listu: "))
for i in range(0, size):
    oldlist.append(random.randint(0, 20))
newlist = []
print(oldlist)
print(*oldlist, sep=', ')

while True:
    useradd = int(input("\nPřidejte libovolné číslo do listu (zadáním záporného čísla přestanete přidávat čísla): "))
    if useradd < 0:
        break
    else:
        oldlist.append(useradd)
        print(oldlist)

b = -1
while True:
    for i in range(len(oldlist)):
        a = oldlist[i]
        if a > b:
            b = a
            index = i
        elif a < b:
            pass
        else:
            b = a
    newlist.append(b)
    b = -1
    if len(oldlist) != 0:
        oldlist.pop(index)
    else:
        break
    print(f"{oldlist}\n{newlist}")
print("fin")