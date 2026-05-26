import random

while False:
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

def generation(name):
    HP = random.randint(5,35)
    kindlist = ["demon", "gnome", "chicken nugget"]
    kind = random.choice(kindlist)
    return f"Foe {name} is a {kind} with {str(HP)} HP."

def open_menu():
    print("-- Menu --\n1 - Create character\n2 - End")

while True:
    open_menu()
    choice = int(input("\n"))
    if choice == 1:
        print(generation(str(input("Choose a name.\n"))))
    elif choice == 2:
        print("-- Turning off --")
        break
    else:
        print("-- Error: Incorrect input --")