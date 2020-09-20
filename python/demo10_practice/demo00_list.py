#切片操作
list = [10, 20, 30, 40, 50]
#1到3，最后面的1为步长
list_2 = list[1:3:1]
#print(list_2)

#判断是否存在
#print(20 in list)
#print(200 in list)

#列表生成
lst = [i * i for i in range (1, 10)]
print(lst)
