x = int(input("Zadejte první číslo "))
y = int(input("Zadejte první číslo "))

if not x != y:
    print("Zadali jste stejná čísla.")
elif x < y:
    print(f"{x} je menší než {y}.")
else:
    print(f"{x} je větší než {y}.")