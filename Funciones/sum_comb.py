from itertools import combinations

def sum_comb(list_n, sum_n=0):
        temp = combinations(list_n,2)  #guarda la 
        for i in list(temp):
            sum_n+=sum(i)
          # print(i,"=",sum(i)) muestra la suma de las comb
        return  sum_n
