### De esta forma podemos llamar a nuestro modulo arias
from Modulos import Modulo_Areas as ma ## Podemos definir un Alias para invocarlo mas facilmente
### Veamos el ejemplo
area_circulo = ma.circulo(2)
print(f"El area de un circulo es {area_circulo}")
area_circulo = ma.circulo(5)
print(f"El area de un circulo es {area_circulo}")