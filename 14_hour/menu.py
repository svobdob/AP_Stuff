import random

while True:
    def naming(name):
        health = random.randint(1, 31)
        species = ["wolf", "zombie", "spirit", "smurf", "gnome", "demon"]
        individual = random.choice(species)
        return f"Foe {name} is a {individual} with {health}HP."

    def menu(choice):
        if choice == "1":
            return naming(input("Name? "))
        else:
            return "Incorrect choice"

    choose = input("1 = Vytvoř postavu\n2 = Konec hry ")
    if choose == "2":
        break
    else:
        pass
    print(menu(choose))