choice = int(input("Jaký kód využijeme (1/2): "))

if choice == 1:
    x = int(input("Zadej číslo: "))
    cont = True
    max = 0

    while cont:
        if x == 0:
            cont = False
            break
        elif max < x:
            max = x
        else:
            max = max
        x = int(input("Zadej číslo:"))

    print(f"Největší uvedené číslo bylo ", max)

    ## Alt
else:
    x = int(input("Zadej číslo: "))
    max = 0

    while x != 0:
        if max < x:
            max = x
        else:
            max = max
        x = int(input("Zadej číslo: "))

    print(f"Největší uvedené číslo bylo ", max)