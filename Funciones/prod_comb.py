from itertools import combinations
from math import prod

def prod_comb(list_n, sum_n=0):
        temp = combinations(list_n,2)  #guarda la 
        print(temp)
        for i in list(temp):
            sum_n+=prod(i)
            print(i,"=",prod(i))
        print("Suma del producto de las combinaciones = ", sum_n)
