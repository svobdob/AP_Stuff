max = "o"
min = "o"
times = int(input("Kolik čísel porovnáme: "))

for i in range(times):
    x = int(input("Zadej číslo: "))
    if max == "o":
        max = x
    elif max < x:
        max = x
    else:
        pass
    if min == "o":
        min = x
    elif min > x:
        min = x
    else:
        pass

print(f" Největší číslo bylo", max, "\n Nejmenší číslo bylo", min)

## Alt

firstpass = True

times = int(input("Kolik čísel porovnáme: "))

for i in range(times):
    x = int(input("Zadej číslo: "))
    if firstpass:
        max = x
    elif max < x:
        max = x
    else:
        pass
    if firstpass:
        min = x
    elif min > x:
        min = x
    else:
        pass
    firstpass = False

print(f" Největší číslo bylo", max, "\n Nejmenší číslo bylo", min)

## Alt 2

times = int(input("Kolik čísel porovnáme: "))
max = int(input("Zadej číslo: "))
min = max

for i in range(times - 1):
    x = int(input("Zadej číslo: "))
    if max < x:
        max = x
    else:
        pass
    if min > x:
        min = x
    else:
        pass

print(f" Největší číslo bylo", max, "\n Nejmenší číslo bylo", min)