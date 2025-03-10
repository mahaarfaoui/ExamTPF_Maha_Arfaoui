def somme(L):
    s = 0
    for e in L:
        s += e
    return s

my_list = [1, 5, 7]
som = somme(my_list)
print('La somme est =', som)
