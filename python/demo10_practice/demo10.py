# def fn (n):
#     return n ** 2
# li = [1, 2, 3, 4, 5]
# print(list(map(fn, li)))

# import random
# print(random.randint(10, 20))

# sum = lambda x, y: x + y
# print(sum(2, 3))

'''
keys是键值， value是内容，items是两个都有
'''
# dic = {"name": "mfh", "age": "23"}
# res = sorted(dic.items(), key = lambda i:i[0])
# print(res)

# import re
# s = "404 Not Found 23 End 测试"
# li = s.split()
# res = re.findall('\d+|[a-zA-Z] + ', s)
# for i in res:
#     if i in li:
#         li.remove(i)
# print(li)

# def fn():
#     try:
#         for i in range(5):
#             if i > 2:
#                 raise Exception("large than 2")
#     except Exception as ret:
#         print(ret)
# fn()

# li = [[1, 2], [3, 4]]
# res = []
# for item in li:
#     res = res + item
# res2 = zip(li)
# print(res)

a = (1, 2, 3, 4)
b = ("a", "b", "c", "d")
a0 = dict(zip(a, b))
a1 = list((range(10)))
a2 = [i for i in a1 if i in a0]
a3 = [a0[s] for s in a0]
a4 = [i for i in a1 if i in a3]
a5 = {i: i * i for i in a1}
a6 = [[i, i * i] for i in a1]
print(a0)
print(a2)
print(a3)
print(a4)
print(a5)
print(a6)
