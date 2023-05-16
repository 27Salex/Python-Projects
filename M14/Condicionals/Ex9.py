actualyear = int(input("Introduce l'año actual (yyyy)"))
otheryear = int(input("Introduce el año a comprobar (yyyy)"))
remaining = actualyear - otheryear

if remaining < 0:
    print("Faltan %d años para llegar al %d" %(abs(remaining), otheryear))
elif remaining > 0:
    print("El año %d fue hace %d años" %(otheryear, remaining))