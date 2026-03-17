num = int(input("Zadejte číslo: "))
soucet = 0

while num != 0:
    soucet += num
    num = int(input("Zadejte číslo: "))

print(f"Výsledek je", soucet)