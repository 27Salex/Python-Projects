import os.path
from cryptography.fernet import Fernet

key = b'NvZqDzXhbe_DpVw8fFAWZb_jNghPakjakUKbaHdTHPQ='
fernet = Fernet(key)

if os.path.isfile('info.txt'):
    choice = input('Do you want to "read" or "add" passwords? ')
    if choice == "add":
        archivo_clave = open('key.txt', 'rb')
        key = archivo_clave.read()
        archivo_clave.close() # cierra el archivo clave después de leerlo
        
        fernet = Fernet(key)
        
        website = input("For what is your password? ")
        userName = input("Please enter the user name: ")
        password = input("Please enter the password here: ")
        encrypted_username = fernet.encrypt(userName.encode())
        encrypted_password = fernet.encrypt(password.encode())
        encrypted_web = fernet.encrypt(website.encode())
        usrnm = encrypted_username + "\n"
        pwd = encrypted_password + "\n"
        web = + encrypted_web + "\n"
        with open("info.txt", 'ab') as file: # utiliza 'ab' para abrir el archivo en modo binario y añadir contenido al final
            file.write("---------------------------------\n".encode())
            file.write(web)
            file.write(usrnm)
            file.write(pwd)
            file.write("---------------------------------\n".encode())
            file.write("\n".encode())
    elif choice == 'read':
        with open("info.txt", 'rb') as file: # abre el archivo en modo binario para leer el contenido cifrado
            contenido_cifrado = file.read()
        contenido_desencriptado = Fernet.decrypt(contenido_cifrado).decode() # decodifica el contenido desencriptado
        print(contenido_desencriptado)
else:
    print("El archivo 'info.txt' no existe")
