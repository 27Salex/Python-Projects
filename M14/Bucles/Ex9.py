numero = int(input("introdueix un numero enter: "))
print("*" * numero)
for i  in range(numero -2):
    print("*", " " * (numero-2) , "*")
print("*" * numero)