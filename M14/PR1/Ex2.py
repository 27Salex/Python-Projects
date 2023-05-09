print("Calculadora IMC")
Altura = float(input("Introdueix la teva alçada en metres:   "))
Pes = float(input("Introdueix el teu pés en kilograms:   "))
Imc= Pes / Altura**2
print(" El teu IMC és: %10.3f"%(Imc))