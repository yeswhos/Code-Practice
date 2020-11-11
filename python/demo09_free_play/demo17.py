import numpy as np
def function(n, q):
    num = len(q)
    arr = np.empty([num, 4], dtype = int)
    point = np.empty([1][1], dtype = int)
    point[0][0] = n
    while point[0][0] > 8:
        point[0][0] -= 8
        point.append
    for i in range(0, 2):
        for j in range(0, q):


    #point = np.empty([q, q])
    print(arr)

if __name__ == '__main__':
    function(1,[[0, 0, 0, 0], [-1, -1, 1, 1]])
