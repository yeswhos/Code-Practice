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

# a = (1, 2, 3, 4)
# b = ("a", "b", "c", "d")
# a0 = dict(zip(a, b))
# a1 = list((range(10)))
# a2 = [i for i in a1 if i in a0]
# a3 = [a0[s] for s in a0]
# a4 = [i for i in a1 if i in a3]
# a5 = {i: i * i for i in a1}
# a6 = [[i, i * i] for i in a1]
# print(a0)
# print(a2)
# print(a3)
# print(a4)
# print(a5)
# print(a6)

################################
# foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
# res = sorted(foo, key = lambda x: (x < 0, abs(x)))
# print(res)
#################################

# foo = [{"name":"zs","age":19},{"name":"ll","age":54}]
# res = sorted(foo, key = lambda x: x["name"])
# res_2 = sorted(foo, key = lambda x: (x[""]))

# li = {"name": "mfh", "age" : "23", "city" : "chengdu"}
# a = zip(li.keys(), li.values())
# b = [i for i in a]
# c = sorted(b, key = lambda x : x[0])
# #print(c)
# new_dic = {x[0] : x[1] for x in c}
# print(new_dic)

import re
# s = "info:xiaoZhang 33 shandong"
# res = re.split(r":| ", s)
# print(res)

# email_list = ["abcghll@163.com", "sdagfr23@163.com", ".com.oefsdj@163"]
# for email in email_list:
#     ret = re.match("[\w]{4, 20}@163\.com$", email)
#     if ret:
#         print("babababa" + ret.group())
#     else:
#         print("lalalala " + email)

# def sum_num(a):
#     if a >= 1:
#         b = a + sum_num(a - 1)
#     else:
#         b = 0
#     return b
#
# print(sum_num(10))

# import re
# s = "年龄23，工资00000"
# res = re.search(r"\d+", s)
# print(res.group())
# res_2 = re.findall("工资", s)
# res_3 = re.findall(r"\d+", s)
# res_4 = re.match("年龄", s)
# print(res_4.group())

# print("{} is {} years old".format("mfh", 23))
# print("%s is %d years old"%("mfh", 23))

# t1 = (("a"), ("b"))
# t2 = (("c"), ("d"))
# res = lambda t1, t2: ({i, j} for i, j in zip(t1, t2))
# print(dict(res(t1, t2)))

# def fn(c):
#     for i in range(c):
#         yield i ** 2
# print(fn(5))

# dic = {"a": 1, "b": 2, "c": 3}
# print(sorted(dic.items(), key = lambda x: x[1], reverse=True))

def fn():
    #return [lambda x: i * x for i in range(4)]
    return [lambda x, i = i: i * x for i in range(4)]
# print(fn())
print([m(2) for m in fn()])

# def mulby(n):
#     def gn(val):
#         return n * val
#     return gn
# a = mulby(7)
# print(a(9))

# s = "       lstrip"
# print(s.lstrip())

# import copy
# li = [[1, 2], [3, 4], [5, 6]]
# new_li = copy.copy(li)
# new_li2 = copy.deepcopy(li)
# # li.append([7, 8])
# li[2][0] = 11
# print(new_li)
# print(new_li2)

# def fn(c):
#     for i in range(c):
#         yield i ** 2
# for item in fn(4):
#     print(item)

# a = [i for i in range(10)]
# b = [lambda : i for i in range(10)]
# print(a)
# #直接输出最后一个数
# print(b[1]())

# print(eval('2 + 3'))

# li = {"name": "mfh", "age" : "23", "city" : "chengdu"}
# res = sorted(li.items(), key = lambda x: (x[0], x[1]))
# print(res)