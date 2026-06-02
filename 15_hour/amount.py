x = 0
y = 0
z = 0

def pripona(num):
    if num == 1:
        return "jednou."
    else:
        return f"{num}krát."
    
def mnozstvi(num):
    if num == 1:
        return "zůstal jeden"
    elif num > 4:
        return f"zůstalo jich {num}"
    elif num == 2 or num == 3 or num == 4:
        return f"zůstali {num}"
    else:
        return "nikdo nezůstal"

while True:
    action = input()
    if action == "e":
        x += 1
        y += 1
        z += 1
    elif action == "l":
        if x == 0:
            print(f"Den končí, v obchodě bylo lidí za celý den {y}, {mnozstvi(x)} a vrata se otevřela {pripona(z)}")
            break
        else:
            x -= 1
            z += 1
    else:
        print(f"Den končí, v obchodě bylo lidí za celý den {y}, {mnozstvi(x)} a vrata se otevřela {pripona(z)}")
        break