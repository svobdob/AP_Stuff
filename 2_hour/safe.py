block = 0
password = "156abd"

while block != 4:
    passinput = str(input("Co je heslo trezoru?"))
    if passinput == password:
        print("Správné heslo.")
    else:
        print("Špatné heslo.")
        block = block + 1