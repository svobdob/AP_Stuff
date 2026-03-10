count = True

while count:
    soucet = 0
    times = int(input("Kolik čísel chcete počítat?"))

    for i in range(times):
        num = int(input("Zadejte číslo"))
        soucet += num
    print(soucet)
    inp = input("Chcete dál počítat? Y/N") ## Annoying
    if inp == "Y":
        print()
    elif inp == "y":
        print()
    else:
        count = False