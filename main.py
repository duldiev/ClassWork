from itertools import permutations


def func(listIn):
    perm = permutations(listIn)
    for i in list(perm):
        print(i)


n = int(input('Enter number of elements: '))
listIn = []
for i in range(n):
    listIn.append(str(input()))

func(listIn)