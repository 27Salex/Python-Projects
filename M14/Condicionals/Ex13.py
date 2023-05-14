num = int(input("Introdueix un número entre 0 i 63: "))
bits = 0

if num == 1 or num == 0:
    bits = 1
elif num < 2**2:
    bits = 2
elif num < 2**3:
    bits = 3
elif num < 2**4:
    bits = 4
elif num < 2**5:
    bits = 5
elif num < 2**6:
    bits = 6
    
print("El nombre de bits necessaris per escriure", num, "en binari és:", bits)