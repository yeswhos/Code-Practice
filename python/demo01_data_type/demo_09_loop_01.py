#for else
for num in [1, 2, 3]:
    print(num)
    if num == 2:
        break
else:
    #循环break，这行就不会执行
    print("here")