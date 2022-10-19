### Librerias necesarias para generar la contraseña
import secrets
import string

############ DEFINICION DEL ALFABETO ########################
letras = string.ascii_letters  ### letras del alfabeto
digitos = string.digits  ####### Digitos del 1 al 9
caracteres = string.punctuation  ## Caracteres especiales

alfabeto = letras + digitos + caracteres  ## Con esto definimos el alfabeto que usaremos

longitud = 12

############# Genera el Password
while True:
    pwd = ''
    for i in range(longitud):
        pwd += ''.join(secrets.choice(alfabeto))

    if any(char in caracteres for char in pwd) and sum(char in digitos for char in pwd) >= 2:
        break

print(pwd)
