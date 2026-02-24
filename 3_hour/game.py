import random

code = int(random.randint(100,999))
safecode = int(random.randint(10000,99999))
tries = 3
escape = False
scissors = False

print("Vítejte ve hře. Jste uzamklý v malé místnosti se stolem, skříní a pár dekorací")
while not escape and tries >= 0:
    print("\nMůžete: \n1 - Kouknout se na stul\n2 - Prohledat skříň\n3 - Podívat se pod koberec\n4 - Otevřít dveře")
    choice = int(input("Co chcete udělat? \n"))

    if choice == 1:
        if scissors:
            print("Už tu nic není.")
        else:
            print("Na stole nic nebylo, ale pod stolem byli malé nůžky.")
            print("Ziskali jste nůžky!")
        scissors = True

    elif choice == 2:
        print("Ve skříni bylo jen pár pavučin a staré oblečení. Ale po delším zkoumání je vidět, že za skříní je prasklina ve zdi.")
        if scissors:
            print("Máš nůžky, chceš zkusit otevřít prasklinu nůžkamy?")
            decide = input("1 = Ano\n")
            if decide == "1":
                print("Povedlo se! Za prasklinou byl ukryt malý sejf, do kterého lze zadat pětimístný kód.")
                decide = input("Chceš zkusit zadat kód? 1 = Ano\n")
                if decide == "1":
                    safechoice = int(input("Zadej kód:\n"))
                    if safechoice == safecode:
                        print(f"Sejf se otevřel a uvnitř byl papírek s číslami.\n", code)
                    else:
                        print("Asi jste zadali špatný kód, jelikož se nic nestalo.")
                else:
                    print()
            else:
                print()
        else:
            print()

    elif choice == 3:
        print(f"Pod kobercem je napsáno na podlaze červenou fixou\n", safecode)

    elif choice == 4:
        print("Dveře jsou uzamknuté, ale vedle nich je malý mechanismus, do kterého můžete napsat kód, který má 3 čísla.")
        unlock = int(input("Zkus zadat kód. \n"))
        if unlock == code:
            print("Dveře se odemkly!")
            escape = True
        else:
            print(f"Dveře jsou stále zamčené. Na textovém poli je napsané\n", tries, "pokusy zbývají.")
            tries = tries - 1
    else:
        print("Neplatný input.")

if escape:
    print("Gratuluji, utekli jste z místnosti!!!")
elif tries >= 0 or tries == 0 or tries != 1 and tries != 2 and tries != 3:
    print("Mechanismus začal blikat červeně a po chvíli explodoval.")
else:
    print("Z nějakého důvodu jsi prohrál.")