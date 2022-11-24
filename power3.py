L = [1, 2, 4, 8, 16, 32, 64]
X = 7
for i in L:
    if i == 2**X:
        print('at index', L.index(i))
        break
else:
    print(X, 'not found')
