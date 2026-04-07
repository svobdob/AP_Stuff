## 7. 4. 2026 - Test Python základy
## Obvod/obsah a sestrojení trojúhelníku

while True:
    uinput = int(input("\nS jakým tvarem chcete pracovat? \n 1 - čtverec | 2 - obdelník | 3 - trojúhelník"))


    if uinput == 1: ## Čtverec
        uinput = input("Chcete počítat obvod nebo obsah?")
        if uinput == "obvod": ## Obvod
            print(f"Počítáte obvod čtverce.")
            a = int(input("Zadejte délku strany a: "))
            vysledek = a * a
            print(f"Obvod čtverce je {vysledek}.")
        elif uinput == "obsah": ## Obsah
            print(f"Počítáte obsah čtverce.")
            a = int(input("Zadejte délku strany a: "))
            vysledek = 4 * a
            print(f"Obsah čtverce je {vysledek}.")
        else:
            print("Chybný input.")


    elif uinput == 2: ## Obdelník
        uinput = input("Chcete počítat obvod nebo obsah?")
        if uinput == "obvod": ## Obvod
            print(f"Počítáte obvod obdelníku.")
            a = int(input("Zadejte délku stranu a: "))
            b = int(input("Zadejte délku stranu b: "))
            vysledek = a * b
            print(f"Obvod obdelníku je {vysledek}.")
        elif uinput == "obsah": ## Obsah
            print(f"Počítáte obsah obdelníku.")
            a = int(input("Zadejte délku stranu a: "))
            b = int(input("Zadejte délku stranu b: "))
            vysledek = 2 * (a + b)
            print(f"Obsah obdelníku je {vysledek}.")
        else:
            print("Chybný input.")


    elif uinput == 3: ## Trojúhelník
        a = int(input("Zadejte délku stranu a: "))
        b = int(input("Zadejte délku stranu b: "))
        c = int(input("Zadejte délku stranu c: "))
        if (a + b) < c or (b + c) < a or (c + a) < b:
            print("Trojúhelník nelze sestavit!")
        else:
            print("Trojúhelník lze sestavit.")
            if a == b and b == c:
                print("Trojúhelník je rovnostranný.")
            elif a == b and b != c:
                print("Trojúhelník je rovnoramenný.")
            elif a != b and b != c and a !=c:
                print("Trojúhelník je různostranný.")
            else:
                print("Trojúhelník je obecný.")


    else:
        print("Chybný input.")
    uinput = input("Chcete počítat ještě něco? Y/N")
    if uinput == "n" or uinput == "N":
        break