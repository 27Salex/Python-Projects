num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))
num3 = int(input("Introdueix el tercer número: "))

if num1 == num2 and num2 == num3:
    print("Els tres números són iguals")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Hi ha dos números iguals")
else:
    print("Els tres números són diferents")
