import random

steps = 1

A = int(input("Zadejte číslo mezi 1 až 6: "))
while True:
    if A >= 7 or A <= 0:
        A = int(input("Zadejte číslo mezi 1 až 6: "))
    else:
        break

print("Random - Vaše")

while True:
    rand = random.randint(1, 6)
    rand2 = random.randint(1, 6)
    rand3 = random.randint(1, 6)
    print(f" {rand} {rand2} {rand3}     {A}")
    if rand == A == rand2 == rand3:
        break
    else:
        steps += 1

print(f"Počet pokusů: {steps}")