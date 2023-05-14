from datetime import date

dia_neix = int(input("Introdueix el dia de naixement: "))
mes_neix = int(input("Introdueix el mes de naixement: "))
any_neix = int(input("Introdueix l'any de naixement: "))


AVUI = date.today()
DIA_ACTUAL = AVUI.day
MES_ACTUAL = AVUI.month
ANY_ACTUAL = AVUI.year

edat = ANY_ACTUAL - any_neix
if MES_ACTUAL < mes_neix:
    edat -= 1
elif MES_ACTUAL == mes_neix and DIA_ACTUAL < dia_neix:
    edat -= 1
    
if edat >= 18:
    print("Ets major d'edat")
else:
    print("Ets menor d'edat")