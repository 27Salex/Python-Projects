# demanar 5 numeros y mostrar la suma
suma = 0
for i  in range(5):
    numero= int(input("Introdueix un numero enter: "))
    if numero > 10:
        suma  +=  numero
print(suma)