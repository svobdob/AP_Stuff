import random

def weapon(adjective):
    weaponlist = ["sword", "bow", "staff", "axe", "crossbow", "shield"]
    bonuslist = ["has higher durability", "grants bonus health points", "speeds up mana regeneration", "lowers skill cooldown", "grants a temporary mana shield", "slowly depletes health points"]
    weapon = random.choice(weaponlist)
    bonus = random.choice(bonuslist)
    durability = random.randint(1, 75)
    return f"You have generated a {adjective} {weapon} that {bonus}, and has {durability} durability."

print(weapon(input("What kind of weapon are you making? (adjective) ")))