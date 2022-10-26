################### CLASES Y OBJETOS EN PYTHON ######################################
class ClaseSilla:
    color = "blanco"
    precio = 100

########### Para declarar un objeto basta con lo siguiente
silla1 = ClaseSilla()
#############################################################################################
print(f"Color silla 1: {silla1.color}, precio silla {silla1.precio}")

### La anterior fue una clase muy sencilla, pero una clase puede tener un constructor
### Tambien puede tener metodos como por ejemplo la siguiente clase

class Persona:
     ###### Esto es un constructor de clases
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    ### Esto es un metodo de una clase
    def saludar(self):
        print(f"Hola soy {self.nombre}  tengo {self.edad}")

### Ahora creamos un objeto persona y llamamos al metodo
### Saludar
persona1 = Persona("Carlos Jose", 29)
persona1.saludar()