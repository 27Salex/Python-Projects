print("Adivina numeros")
num = 23
def tryagain():
    guess = int(input ("Introduce un numero:   "))
    if guess == num:
        print("Has acertado, el numero era 23!")
    else:
        print("Ups parece que has fallado, prueba otra vez!")
        tryagain()
tryagain()