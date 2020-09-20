#创建集合,不允许重复,有序的
s = {1, 2, 3, 4, 5}
print(s)

ss = set(range(6))
#print(ss)

sss = set([1, 2, 3])
print(sss)

print(set((1, 2, 3, 4)))

ssss = set()

#操作
# print(100 in s)
# print(1 in s)
s.add(6)
s.update((7, 8))
print(s)

s.remove(8)
#如果不存在则不会报异常
s.discard(8)
#弹出任意元素，也可能是从小的数字开始删除
a = s.pop()
print(a)
s.clear()

#判断是不是子集
print(s.issubset(ss))

#交集，并集，差集，对称差集
s1 = {10, 20, 30}
s2 = {20, 30, 40, 50}

print(s1.intersection(s2))
print(s1 & s2)

print(s1.union(s2))
print(s1 | s2)

print(s1.difference(s2))
print(s1-s2)

print(s1.symmetric_difference(s2))
print(s1 ^ s2)

#集合生成
s3 = {i * i for i in range(10)}
print(s3)
