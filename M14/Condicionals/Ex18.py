edat1 = int(input("Introdueix l'edat de la primera persona: "))
edat2 = int(input("Introdueix l'edat de la segona persona: "))
edat3 = int(input("Introdueix l'edat de la tercera persona: "))


if edat1 < 5:
    cost1 = 0
elif edat1 >= 5 and edat1 < 12:
    cost1 = 20 * 0.25
elif edat1 >= 12 and edat1 < 16:
    cost1 = 20 * 0.5
elif edat1 >= 16 and edat1 < 65:
    cost1 = 20
else:
    cost1 = 0

if edat2 < 5:
    cost2 = 0
elif edat2 >= 5 and edat2 < 12:
    cost2 = 20 * 0.25
elif edat2 >= 12 and edat2 < 16:
    cost2 = 20 * 0.5
elif edat2 >= 16 and edat2 < 65:
    cost2 = 20
else:
    cost2 = 0

if edat3 < 5:
    cost3 = 0
elif edat3 >= 5 and edat3 < 12:
    cost3 = 20 * 0.25
elif edat3 >= 12 and edat3 < 16:
    cost3 = 20 * 0.5
elif edat3 >= 16 and edat3 < 65:
    cost3 = 20
else:
    cost3 = 0

if edat1 >= 16 and edat1 <= 18 and edat2 >= 16 and edat2 <= 18 and edat3 >= 16 and edat3 <= 18:
    cost_total = 2 * 20 + cost1 + cost2 + cost3
else:
    cost_total = cost1 + cost2 + cost3


print("El cost total de les entrades és de", cost_total, "€.")
