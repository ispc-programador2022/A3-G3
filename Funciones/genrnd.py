# retorna una lista con 50 números aleatorios.

import random

def genrnd(number):
    list_n = []
    for i in range(number):
        list_n.append(random.randrange(100))
    return list_n
