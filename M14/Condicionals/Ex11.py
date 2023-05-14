hores = int(input("Introdueix el nombre d'hores treballades: "))
torn = input("Introdueix el torn (D per diürn, N per nocturn): ")
dia_setmana = input("Introdueix el dia de la setmana (Dl, Dt, Dc, Dj, Dv, Ds, Dg): ")

tarifa = 4
if torn.casefold() == "N":
    tarifa = 6

if dia_setmana.casefold() == "Dg": 
    if torn == "D":
        tarifa = tarifa + 3
    else:
        tarifa = tarifa + 2
        
salari = hores * tarifa
print("El salari es de: ", salari,"€")
     