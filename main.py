def somme(L):
    s = 0
    for e in L:
        s += e
    return s

my_list = [1, 5, 7]
som = somme(my_list)
print('La somme est =', som)

my_list = [1, 5, 7]

print('La somme est =', sum(my_list))

if my_list:
    print('La somme est :', sum(my_list))
    print('Le max est :', max(my_list))
    print('Le min est :', min(my_list))
else:
    print("Liste vide")


