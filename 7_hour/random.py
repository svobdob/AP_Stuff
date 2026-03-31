import random
steps = 0
rand = random.randint(1, 6)
rand2 = 0

while True:
    rand = random.randint(1, 6)
    rand2 = random.randint(1, 6)
    print(f"{rand} {rand2}")
    if rand != rand2:
        steps += 1
    else:
        break





## not it
while rand != rand2:
    break
    if rand != rand2:
        print(f"A {rand} {rand2}")
        rand2 = rand
        steps += 1
        print(f"B {rand} {rand2}")
    else:
        pass
    rand = random.randint(1, 6)

print(f"fin: {rand} {rand2} {steps}")