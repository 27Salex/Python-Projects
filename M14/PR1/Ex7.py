print("Nota final")
notaExercici1 = float(input("Introdueix la nota del PRIMER exercici:  "))
notaExercici2 = float(input("Introdueix la nota del SEGON exercici:  "))
notaExercici3 = float(input("Introdueix la nota del TERCER exercici:  "))
notaExamen = float(input("Introdueix la nota del examen:  "))
notaProva = float(input("Introdueix la nota de la prova practica final:  "))

mitjanaExercicis = (notaExercici1 + notaExercici2 + notaExercici3) / 3


notaFinal = mitjanaExercicis * 0.55 + notaExamen * 0.3 + notaProva * 0.15
print ("La teva nota final es: %2.2f " %(notaFinal))