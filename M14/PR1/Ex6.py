print("Càlculs aritmétics")
pressupost = int(input("Introdueix el pressupost:   "))
pediatria =  pressupost * 0.3
traumatologia =  pressupost * 0.2
ginecologia = pediatria + traumatologia
print ("Amb un pressupost de %d€ , li pertoquen  %d€ a pediatria, %d€ a traumatologia y %d€ a ginecologia." %(pressupost, pediatria,traumatologia, ginecologia)) 