def sum_comb(list_n, sum_n=0):
    if len(list_n) == 2:
        sum_n += list_n[0] + list_n[1]
        return sum_n
    elif len(list_n) < 2:
        print("Debe ser una lista con al menos dos valores")
    else:
        for i in range(len(list_n[1:])):
            sum_n += list_n[0] + list_n[1:][i]
        return sum_comb(list_n[1:], sum_n)
