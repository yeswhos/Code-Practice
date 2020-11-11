def absSort(input_a):
    li = map(int, input_a)
    li = list(sorted(li, key=abs))
    return li

arr = [-9,-3,0,1,2,8,10,14,18]
print(absSort(arr))