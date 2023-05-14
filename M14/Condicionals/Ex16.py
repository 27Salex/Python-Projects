from random import randint
dau1=randint(1,6)
dau2=randint(1,6)
dau3=randint(1,6)

if dau1 == 6 and dau2 == 6 and dau3 == 6:
    print("Excel·lent")
elif (dau1 == 6 and dau2 == 6) or (dau1 == 6 and dau3 == 6) or (dau2 == 6 and dau3 == 6):
    print("Molt bé")
elif dau1 == 6 or dau2 == 6 or dau3 == 6:
    print("Regular")
else:
    print("Pèssim")