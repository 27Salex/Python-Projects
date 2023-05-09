horesJocs = int(input("Escriu les hores que pases jugant a videojocs:   "))
horesEstudiant = int(input("Escriu les hores que pases estudiant:   "))
horesDormint = int(input("Escriu les hores que pases dormint:   "))
horesEsport = int(input("Escriu les hores que pases fet esport:   "))
totalHores = horesDormint + horesEsport + horesJocs + horesEstudiant
if totalHores <= 24:
    horesRestants = 24 - totalHores
    print("Et queden %dh per a dedicar-te a altres coses" %(horesRestants))
else:
    print("Error, el dia només te 24h torna a intentar-ho")