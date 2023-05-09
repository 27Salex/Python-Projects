
print("Calculador de sous")
neteja = int(input("Introdueix el numero de personal de neteja:  "))
auxAdmin = int(input("Introdueix el numero d'auxiliars administratius:  "))
administratius = int(input("Introdueix el numero d'administratius:  "))
informatics = int(input("Introdueix el numero d'informatics  "))
consultantSenior = int(input("Introdueix el numero de constultants senior:  "))

sousA = 500 * neteja
sousB = 600 * auxAdmin
sousC = 700 * administratius
sousD = 1200 * informatics
sousE = 12000 * consultantSenior
souTotal = sousA + sousB + sousC + sousD + sousE
souTotal = int(souTotal)
print("El sou total del personal de neteja es: ", sousA, "€ mensuals")
print("El sou total dels auxiliars administratius es de: ", sousB, "€ mensuals")
print("El sou total dels administratius es de: ", sousC, "€ mensuals")
print("El sou total dels informatics es de: ", sousD, "€ mensuals")
print("El sou total dels consultants senior es de: ", sousE, "€ mensuals")
print("El sou TOTAL a pagar es de:", souTotal, "€ mensuals")