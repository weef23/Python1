##############################################################################################################
###### Ejemplo de funciones en Python

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