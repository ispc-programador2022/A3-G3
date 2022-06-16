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
from Funciones.p1 import p1_1, p1_2, p1_3
from Funciones.genrnd import genrnd
from Funciones.sum_comb import sum_comb
from Funciones.prod_comb import prod_comb

# Bienvenida
bienvenida()

# Ingreso de dos valores enteros y asignación a la variable 'nums'
nums = ing2i()

# Operación suma
print("\n***Función Suma***")
print("Suma = ", suma(nums[0], nums[1]))

# Operación resta
print("\n***Función Resta***")
print("Resta = ", resta(nums[0], nums[1]))

# Operacion producto
print("\n***Función Producto***")
print("Producto = ", producto(nums[0], nums[1]))

# Operación cociente
print("\n***Función Cociente***")
print("Cociente = ", cociente(nums[0], nums[1]))

# Operación módulo
print("\n***Función Módulo***")
print("Módulo = ", modulo(nums[0], nums[1]))

# Operación potencia
print("\n***Función Potencia***")
print("Potencia = ", potencia(nums[0], nums[1]))

# Operación radicación
print("\n***Función Radicación***")
print("Raiz = ", radicacion(nums[0], nums[1]))


#Ingreso del 3er número. Se agrega al final de la lista Nums
nums.append(int(input("\nIngrese un 3er valor entero: ")))  
print("N1=",nums[0],"  N2=", nums[1],"  N3=",nums[2])  

# Producto de los dos primeros más el 3er valor
print("\n***Producto de los dos primeros más el 3er valor***")
print("Resultado = ", p1_1(nums[0], nums[1], nums[2]))

# Suma de los dos primeros por el 3er valor
print("\n***Suma de los dos primeros por el 3er valor***")
print("Resultado = ", p1_2(nums[0], nums[1], nums[2]))

# Resta de los dos primeros por el 3er valor
print("\n***Resta de los dos primeros por el 3er valor***")
print("Resultado = ", p1_3(nums[0], nums[1], nums[2]))

# # Ingreso de dos valores string
print("\nCadenas= ", ing2s())

# retorna una lista con 50 números aleatorios.
print("\n***Retorna una lista con 50 números aleatorios***")
list50 = genrnd(50)
print(list50)

# A partir de esta función se utilizará list50

# Suma de las combinaciones
print("\n***Devuelve la suma de las combinaciones posibles de los números generados por la función genrnd tomados de a dos.***", sum_comb(list50), sep="\n")

# Producto de las combinaciones
print("\n***Devuelve el producto de las combinaciones posibles de los números generados por la función genrnd tomados de a dos.***", prod_comb(list50), sep="\n")