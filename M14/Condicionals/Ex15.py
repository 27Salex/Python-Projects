num = input("Introdueix un número enter positiu: ")

if not isinstance(num, int):
    print("Error: has d'introduir un número")
elif num < 0:
    print("Error: has d'introduir un número enter positiu")
elif num < 10:
    print("El número té 1 xifra")
elif num < 100:
    print("El número té 2 xifres")
elif num < 1000:
    print("El número té 3 xifres")
elif num < 10000:
    print("El número té 4 xifres")
else:
    print("El número no esta en el rang")