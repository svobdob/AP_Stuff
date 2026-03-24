while(True):
    x = int(input("Zadejte číslo: "))
    y = 0
    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = x * 3 + 1
        print(f" Číslo se změnilo na:", x)
        y = y + 1

    print(f"Bylo potřeba", y, "průchodů")
    choice = input("Chcete pokračovat? (Y/N) ")
    if choice.lower() ==  "n":
        break
    else:
        pass