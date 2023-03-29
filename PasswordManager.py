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
        usrnm = "UserName: " + encrypted_username.decode() + "\n"
        pwd = "Password: " + encrypted_password.decode() + "\n"
        web = "Website: " + website + "\n"
        with open("info.txt", 'ab') as file: # utiliza 'ab' para abrir el archivo en modo binario y añadir contenido al final
            file.write("---------------------------------\n".encode())
            file.write(web.encode())
            file.write(usrnm.encode())
            file.write(pwd.encode())
            file.write("---------------------------------\n".encode())
            file.write("\n".encode())
    elif choice == 'read':
        with open("info.txt", 'rb') as file: # abre el archivo en modo binario para leer el contenido cifrado
            contenido_cifrado = file.read()
        contenido_desencriptado = fernet.decrypt(contenido_cifrado).decode() # decodifica el contenido desencriptado
        print(contenido_desencriptado)
else:
    print("El archivo 'info.txt' no existe")
