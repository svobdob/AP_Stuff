length = int(input("Last number: "))
originlist = list(range(1,length+1))
evenlist = []
oddlist = []
print(f"Original: {originlist}")

for num in originlist:
    if num % 2 == 0:
        evenlist.append(num)
    else:
        oddlist.append(num)

print("Even: ", *evenlist, sep="/", end="\n")
print("Odd: ", *oddlist, sep="/")