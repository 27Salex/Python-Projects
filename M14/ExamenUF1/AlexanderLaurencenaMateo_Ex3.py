print("Calcul Descompte")
preuProducte =  float(input("Escriu el preu del producte:   "))
descompte =  float(input("Escriu el descompte a aplicar (de 0 - 100):   ")) / 100
preuFinal = preuProducte - preuProducte* descompte
print("El preu final és de: ", preuFinal)
