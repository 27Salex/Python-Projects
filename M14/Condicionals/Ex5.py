edad = int(input("introduce tu edad:   "))
ingresos = int(input("introduce tus ingresos mensuals:   "))
if edad > 16 and ingresos > 1000:
    print("Tendras de tributar")
else:
    print("No tendras que tributar")