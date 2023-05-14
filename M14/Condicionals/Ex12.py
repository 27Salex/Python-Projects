num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))
operacio = input("Introdueix l'operació (+, -, *, /, //, %): ")

if operacio == "+":
    resultat = num1 + num2
    print("El resultat de l'operació és: ", resultat)
elif operacio == "-":
    resultat = num1 - num2
    print("El resultat de l'operació és:  ", resultat)
elif operacio == "*":
    resultat = num1 * num2
    print("El resultat de l'operació és:  ", resultat)
elif operacio == "/":
    resultat = num1 / num2
    print("El resultat de l'operació és:  ", resultat)
elif operacio == "//":
    resultat = num1 // num2
    print("El resultat de l'operació és:  ", resultat)
elif operacio == "%":
    resultat = num1 % num2
    print("El resultat de l'operació és:  ", resultat)
else:
    print("Operació no vàlida")