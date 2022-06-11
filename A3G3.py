# A3G3

from Funciones.bienvenida import bienvenida
from Funciones.ing2i import ing2i
from Funciones.suma import suma
from Funciones.ing2s import ing2s
from Funciones.resta import resta
from Funciones.producto import producto
from Funciones.cociente import cociente
from Funciones.modulo import modulo
from Funciones.potencia import potencia
from Funciones.radicacion import radicacion
from Funciones.prueba import prueba

# Bienvenida
bienvenida()

# Ingreso de dos valores enteros y asignación a la variable 'nums'
nums = ing2i()

# Operación suma
print("Suma = ", suma(nums[0], nums[1]))

# Operación resta
print("Resta = ", resta(nums[0], nums[1]))

# Operacion producto
print("Producto = ", producto(nums[0], nums[1]))

# Operación cociente
print("Cociente = ", cociente(nums[0], nums[1]))

# Operación módulo
print("Módulo = ", modulo(nums[0], nums[1]))

# Operación potencia
print("Potencia = ", potencia(nums[0], nums[1]))

# Operación radicación
print("Raiz = ", radicacion(nums[0], nums[1]))

# Ingreso de dos valores string
<<<<<<< HEAD
print("Cadenas= ", ing2s())
=======
print("Cadenas= ", ing2s())

# Ingreso de dos valores string ----- duplicado
print("Cadenas= ", ing2s())

prueba ()
>>>>>>> 22de27c232a87af7e4079429f59cefe61d760dcb
