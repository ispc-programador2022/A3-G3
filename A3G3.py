#A3G3

from Funciones.bienvenida import bienvenida
from Funciones.ing2i import ing2i 
from Funciones.suma import suma
from Funciones.ing2s import ing2s
from Funciones.resta import resta
from Funciones.producto import producto

#Bienvenida
bienvenida()

#Ingreso de dos valores enteros y asignación a la variable 'nums'
nums = ing2i()

#Operación suma
print("Suma = ", suma(nums[0], nums[1]))

#Operación resta
resta()

#Ingreso de dos valores string
print("Cadenas= ",ing2s())

#Operacion producto
producto()
