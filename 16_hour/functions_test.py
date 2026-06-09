######### Functions - 9.6.2026
######### Shopping

cart = [120,50,200,890,15]

def costcalc(kosik):
    cost = 0
    for i in range(len(kosik)):
        cost += kosik[i]
    return cost

def expensive(kosik):
    max = 0
    for i in range(len(kosik)):
        if max < kosik[i]:
            max = kosik[i]
        else:
            pass
    return max

def filter(kosik, limit):
    filtered = []
    for i in range(len(kosik)):
        if limit > kosik[i]:
            filtered.append(kosik[i])
        else:
            pass
    return filtered

def sale(kosik, sleva, limit):
    if limit >= costcalc(kosik):
        return costcalc(kosik) - costcalc(kosik)*sleva
    else:
        return costcalc(kosik)

print(f"Košík: {cart}\nCena: {costcalc(cart)} Kč\nNejdražší: {expensive(cart)} Kč\nPoložky levnější než 500: {filter(cart, 500)}\nKonečná cena (popř. se slevou): {sale(cart, 0.1, 2000)} Kč")