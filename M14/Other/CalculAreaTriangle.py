print("Programa Càlcul de l'àrea d'un triangle")
#Afaga la base
base =  float(input("Mida de la base:   "))

#Afaga l'altura
Altura = float(input("Alçada del triangle:   "))

# Calcul de l'area
area = base * Altura / 2
print("El resultat és:", area)
print("La base és: %6.2f i l'àrea és %f " %( base,area)) # %f , remplaza en orden los valores dentro de %(), y los cambia a tipo float. El %6.2f, hace que se imprima el valor en float, con 6 enteros y 2 decimales
print("La base és: %d i l'àrea és %d i la àrea és %d50" %( base,area,area)) # %d , remplaza en orden los valores dentro de %(), y los cambia a tipo integer