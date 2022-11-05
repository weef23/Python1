######################### FUNCIONES LAMBDA EN PYTHON ########################################
from functools import  reduce
### Estructura de una expresion Lambda argumentos  + expresion

### Lo que hace el siguiente ejemplo es recibir un String y compararlo con el String al reves
palindrome = lambda string : string==string[::-1]

## La funcion anonima es llamada por medio de la varible que almacena la funcion
print(palindrome('ana'))
## Las funciones lambda son funciones pequeñas constan de uno o varios parametros y una expresion.
## Son funciones anonimas pero asignadas a una variable como se vio anteriormente.
## No se requiere parentesis, no se necesita un return pero deben retornar una funcion valida
## lo que esta a la izquierda de los dos puntos son los parametros y a la derecha la expresion
resultado = lambda a, b: a+b

print(f"Resultado de sumar con funsion lambda {resultado(4,6)}")

## Tambien podemos definir una funcion lambda sin argumentos como acontinuacion
funcion_sin_argumentos = lambda : 'Esta funcion no tiene argumentos'
print(funcion_sin_argumentos())

## Al igual que en una funcion normal podemos asignar parametros por defectos.
resultado2 = lambda a=3, b=5 : a*b
print(f"El resultado de pasarlo sin parametros es {resultado2()} y si lo paso con parametros {resultado2(5,8)}")

### Parametros variables
## Los Kwarg representan un diccionario local con un indeterminado numero de elementos van precedido de **
## Los arg son parametros variables indeterminados.
resultado3 = lambda *args, **kwargs: len(args) + len(kwargs)

print(f"Funcion lambda con parametros varibles {resultado3(1,2,3,a=3,b=4)}")

##### Uso de las funciones Map y reduce
lista = [2,2,2,2,2]

## Esta funcion reduce lo que hace es tomar una lista o iterable y reducirlo a un unico valor
## En este caso toma como parametro la funcion lambda (lambda a,b:a*b) y una lista
## Procede a realizar la multiplicacion
multiplicacion = reduce(lambda a,b:a*b,lista)
print(multiplicacion)

## Funcion Map en Python
## En el ejemplo anterior hicimos la multiplicacion sucesiva de los valores de una lista pero veamos otro ejemplo
numeros = [2,3,4,5,6]

duplica_nuemero = map(lambda a: a*2, numeros)
## la funcion map nos devuelve por defecto un objeto iterable pero que podemos transformarlo en una lista
## Basicamente recorrimos una lista y multiplicamos cada valor por dos
print(list(duplica_nuemero))
## Veamos un ejemplo utilizando dos listas

lista1= [2, 4, 6, 8, 10]
lista2= [1, 3, 5, 7, 9]
## Esto nos ayuda a reducir muchisomo el codigo evitando ciclos y crear una funcion.
multiplicacionListas = list(map(lambda a, b: a*b, lista1,lista2))

print(multiplicacionListas)