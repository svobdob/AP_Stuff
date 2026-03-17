while():
    break
    a = int(input("Zadejte první číslo: "))
    b = int(input("Zadejte druhé číslo: "))

    while b == 0:
        print("Nelze dělit 0!")
        b = int(input("Zadejte nové druhé číslo: "))

    soucet = a + b
    rozdil = a - b
    nasobe = a * b
    deleni = a / b

    print(f"Výsledky: \nSoučet je", soucet, "\nRozdíl je", rozdil, "\nNásobení je", nasobe, "\nDělení je", deleni)

    c = input("\nChcete pokračovat? (Y/N) ")
    if c.lower() == "y":
        break
    else:
        pass
## alt

while(True):
    break
    a = int(input("Zadejte první číslo: "))
    b = int(input("Zadejte druhé číslo: "))

    choice = int(input("Co chcete dělat?\n 1 = Součet, 2 = Rozdíl, 3 = Násobení, 4 = Dělení "))
    if choice == 1:
        answer = a + b
    elif choice == 2:
        answer = a - b
    elif choice == 3:
        answer = a * b
    elif choice == 4:
        while b == 0:
            print("Nelze dělit 0!")
            b = int(input("Zadejte nové druhé číslo: "))
        answer = a / b
    else:
        print("Invalidní volba")
    
    print(f"Výsledek je ", answer)

    c = input("\nChcete pokračovat? (Y/N) ")
    if c.lower() == "n":
        break
    else:
        pass
## alt2
    
while True:
    a = int(input("Zadejte první číslo: "))
    b = int(input("Zadejte druhé číslo: "))

    equation = input("Co chcete dělat? \n1 = Součet, 2 = Rozdíl, 3 = Násobení, 4 = Dělení ")
    match equation:
        case "1": answer = a + b
        case "2": answer = a - b
        case "3": answer = a * b
        case "4":
            while b == 0:
                print("Nelze dělit 0!")
                b = int(input("Zadejte nové druhé číslo: "))
            answer = a / b
    print(f"Výsledek je ", answer)

    c = input("\nChcete pokračovat? (Y/N) ")
    if c.lower() == "y":
        break
    else:
        pass