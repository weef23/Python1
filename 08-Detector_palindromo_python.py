####### utilizando las funciones y los metodos de cadena detectamos
####### si la cadena es un palindromo o no lo es.
def esPalindromo(palabra):
    ##la convertimos en mayuscula
    palabra = str(palabra).strip().lower().replace(' ','')
    ###Validamos si la cadena es igual al derecho y al reves
    if(palabra[::] == palabra[::-1]):
        return True
    else:
        return False
### Funcion principal del programa es como el main de c y c++
def run():
    ##############################################################################
    palabra = input("Ingrese la cadena que desea verificar: \n")
    if (esPalindromo(palabra)):
        print("La cadena introducida es un palindromo")
    else:
        print("La cadena introducida no es un palindromo")

### Entry point del programa, indica el punto de inicio del programa
if __name__ == '__main__':
    run()



