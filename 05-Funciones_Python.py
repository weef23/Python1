##############################################################################################################
###### Ejemplo de funciones en Python
from functools import  reduce
## Para definir una funcion usamos la palabra def
## Este es un ejemplo de una funcion basica, no recibe parametros ni retorna valores
## Solo ejecuta un fragmento de codigo

def imprimirMensaje():
    print("Mensaje especial: ")
    print("Estoy aprendiendo a usar funciones: ")

#### La siguiente opcion recibe como parametro una opcion
def seleccionarMensaje(opcion):

        print("Hola")
        print("Como estas?")
        print(f"Elegiste la opcion {opcion}")

#### La Siguiente funcion es un ejemplo de una funcion que recibe parametros y
### Devuelve resultados
def suma(a,b):
    print("Se suman dos numero: ")
    resultado = a + b
    return resultado

###### USO DE ARGUMENTOS VARIABLES
## Los argumentos variables de una funcion van precedidos de un asterisco *
## Si bien se puede usar cualquier nombre se recomienda el uso de *args
def lista_Nombre(*args):
    for nombre in args:
        print(f"Hola {nombre}")

## Ejemplo de suma usando *arg
def suma_Numeros(*args):
    return reduce(lambda a, b: a+b, args) ## Es muy util realizar esto con reduce

## Otra ventaja interesande de Python son los parametros dinamicos clave valor
## Para declarar este tipo de argumentos es necesario colocar dos **  antes del nombre
def lista_Terminos(**terminos):
    for llave,valor in terminos.items():
        print(f"Llave {llave}  => Valor {valor}")

###############################################################################################################
## Invocacion de la funcion de imprimir mensaje
imprimirMensaje()

### Invocar funcion con parametros

opcion = input("Elige una opcion (1,2,3): ")

if(opcion == '1'):
    seleccionarMensaje(opcion)
elif(opcion == '2'):
    seleccionarMensaje(opcion)
elif(opcion == '3'):
    seleccionarMensaje(opcion)
else:
    print("Elija la opcion correcta")

resultado = suma(2,3)
print(resultado)

## Podemos enviar mas de un valor a la vez
lista_Nombre("Juan", "Pedro", "Jose")
## Ejemplo de suma usando args
print(f"La suma de valores {suma_Numeros(1,2,3,4,5)}")

lista_Terminos(Nombre="Jose", Apellido="Martinez", Edad="18")