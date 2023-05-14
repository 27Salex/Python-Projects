num1 = input("Introdueix un número enter positiu: ")
num2 = input("Introdueix un segon número enter positiu: ")
num3 = input("Introdueix un tercer número enter positiu: ")


def errorCheck():
    global num1, num2, num3
    if num1.isdigit():
        num1 = int(num1)
    else:
        print("ERROR: El primer número, no es un número enter positiu i sense caracters.")
        exit()

    if num2.isdigit():
        num2 = int(num2)
    else:
        print( "ERROR: El segon número, no es un número enter positiu i sense caracters.")
        exit()
        
    if num3.isdigit():
        num3 = int(num3)
    else:
        print("ERROR: El tercer número, no es un número enter positiu i sense caracters.")
        exit()

    if num1 < 0:
        print("ERROR: El primer número es inferior a 0")
        exit()
    elif num2 < 0:
        print("ERROR: El segon número es inferior a 0")
        exit()
    elif num3 < 0:
        print("ERROR: El tercer número es inferior a 0")
        exit()
    if num1 == num2 or num1 == num3 or num3 == num2:
        print("ERROR: Hi ha 2 o més numeros iguals")
        exit()
    
errorCheck()

llista = [num1, num2, num3]
llista_ordenada = sorted(llista, reverse=True)

print(llista_ordenada)