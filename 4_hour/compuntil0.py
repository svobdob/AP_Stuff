x = int(input("Zadej číslo: "))
cont = True
max = 0

while cont:
    if x == 0:
        cont = False
        break
    elif max < x:
        max = x
    else:
        max = max
    x = int(input("Zadej číslo:"))

print(f"Největší uvedené číslo bylo ", max)