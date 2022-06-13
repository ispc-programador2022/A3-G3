from Funciones.producto import producto
from Funciones.suma import suma
from Funciones.resta import resta


# Función p1, retorna el producto de dos valores mas un tercer valor
def p1_1(a, b, c):
    prod = producto(a, b)
    sum = suma(prod, c)
    print( "(",a,"x",b,") + ",c,)
    return sum

# Función p2, retorna la suma de dos valores por un tercer valor
def p1_2(a, b, c):
    sum = suma(a, b)
    prod = producto(sum, c)
    print( "(",a,"+",b,") x ",c,)
    return prod

# Función p3, retorna la resta de dos valores por un tercer valor
def p1_3(a, b, c):
    res = resta(a, b)
    prod = producto(res, c)
    print( "(",a,"-",b,") x ",c,)
    return prod
