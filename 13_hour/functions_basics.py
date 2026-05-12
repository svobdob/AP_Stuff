def greeting1(name):
    result = f"Welcome, {name}."
    return result

print(greeting1("Bob"))

#####

def greeting2(name):
    return f"Welcome {name}."

print(greeting2("BbBbBBbbb"))

#####

def decide(name, age):
    if age < 12:
        return f"{name} isn't old enough."
    else:
        return f"{name} is old enough."

print(decide("feef", 78))

#####

def fight(defense, attack):
    if attack < defense:
        return f"You were hit!"
    else:
        return f"You deflected the attack!"

print(fight(int(input("Defense: ")), int(input("Attack: "))))

#####

def count(numbers):
    vysledek = 0
    for i in range(0, len(numbers)):
        vysledek += numbers[i]
    return vysledek

field = []
while True:
    add = int(input("Add a number (by adding a negative number you stop adding): "))
    if add < 0:
        break
    else:
        field.append(add)

print(count(field))

#####

batoh = ["lektvar", "klacek", "blbost", "meč", "blbost", "štít", "lektvar", "blbost"]

def howmuch(array, item):
    quantity = 0
    for i in range(0, len(array)):
        if array[i] == item:
            quantity += 1
        else:
            pass
    return quantity

predmet = input("What are we looking: ")
print(f"{predmet}: {howmuch(batoh, predmet)}.")