######################################CONJUNTOS EN PYTHON##################################################
##### Ejemplo de conjuntos, la estructura es similar a un diccionario sin embargo no posee Clave valor
paises = {"Mexico", "Guatemala", "El Salvador", "Costa Rica", "Colombia"}
print(paises)

#### Los conjuntos tienen la ventaja de que no se repiten, por ejemplo si yo pongo Mexico dos veces
#### Al momento de hacer un print este no se repetira.
paises = {"Mexico", "Mexico", "Guatemala", "El Salvador", "Costa Rica", "Colombia"}
print(paises)

### Adminte mas de un tipo de datos al igual que las listas.
### Los conjuntos no tienen un orden especifico
conjuntos_mixtos = {1, 'hola', False, 12.12} ## Recordemos que en Python todo es una clase
print(conjuntos_mixtos)
print(type(conjuntos_mixtos))

## Con el metodo set podemos ser capaces de crear un conjunto de otras estructuras
## Lo podemos crear a partir de un string
conjunto_cadena = set('hoola')
print (conjunto_cadena)

## A traves de una Tupla
conjunto_tupla = set(("aa", "ab", "bb", "bc"))
print(conjunto_tupla)

## De una lista
conjunto_lista = set([1, 1, 2, 3, 4, 4, 5, 6, 7, 8])
print(conjunto_lista)
#### Lo podemos convertir a una lista
list_conjunto = list(conjunto_lista)
print (conjunto_lista)
#################### OPERACIONES CON CONJUNTOS ##############################

paises = {"Mexico", "Guatemala", "El Salvador", "Costa Rica", "Colombia"}
### Verificar tamaño
tamaño = len(paises) #El len funciona para cualquier estrutura.


### Validar si un elemento es parte de un conjunto
print('Mexico' in paises)
print('Peru' in paises)

### Agregar un elemento a un cojunto
paises.add('Peru')
## Ahora peru si esta en el conjunto
print('Peru' in paises)

## Actualizar Elemento
## Funciona mas o menos igual que add para me permita pasar una lista
paises.update({"Nicaragua","Honduras","Bolivia"})
print(paises)
### Eliminar
paises.remove('Nicaragua')
print(paises)
### La funcion discard sirve para evitar un error al intentar eliminar un elemento que no existe
paises.discard('Nicaragua') ## Nicaragua ya no existe.
print(paises)

## Si queremos limpiar un conjunto entero podemos hacer esto
paises.clear()
print(len(paises)) ## Nos devuelve 0

##### OPERACIONES ENTRE CONJUNTOS ######
#### aparte de las operaciones que podemos hacer con los elementos del mismo conjunto
#### tambien podemos realizar operaciones con dos o mas conjuntos

conjunto_1 = {1,3,5,7,9}
conjunto_2 = {2,4,6,8}

###### Union de dos conjuntos
conjunto_union = conjunto_1.union(conjunto_2)
print(conjunto_union)

figuras_geometricas = {"Triangulo", "Cuadrado", "Pentagono", "Hexagono"}
forma = {"Circulo", "Cuadrado","Triangulo","Estrella"}

#### Interseccion de conjuntos
conjunto_interseccion = figuras_geometricas.intersection(forma)
print(conjunto_interseccion)

### Lo que esta en A pero no en B (A-B)
diferencia = forma.difference(figuras_geometricas)
print(diferencia)
### Union omitiendo elementos comunes

simetria = forma.symmetric_difference(figuras_geometricas)
print(simetria)







