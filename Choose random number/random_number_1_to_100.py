
import random

print('\n')
def check():
    with open("detyra.txt") as f:
        lista = [int(x) for x in f.read().split()]

    return lista

for i in range(1, 11):
    num = random.randint(1, 100)

    while num in check():
        num = random.randint(1, 100)
    else:
        f = open('detyra.txt', 'a')
        f.write("{} ".format(num))
        f.close()

print('Numrat jane gjeneruar! Shiko ne fajlin detyra.txt!')
