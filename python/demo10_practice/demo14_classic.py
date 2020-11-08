A0 = dict(zip(('a', 'b', 'c', 'd'), (1, 2, 3, 4)))
A1 = range(10)
A2 = [A0[s] for s in A0]
A3 = [i for i in A1 if i in A2]
print(A3)