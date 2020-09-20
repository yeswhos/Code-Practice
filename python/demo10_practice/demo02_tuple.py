#创建元组
tup = ('jack', 'rose')
tupp = tuple(('jack', 'rose'))
tup_empty = ()
# print(tup)
# print(tupp)

t = (1, [2, 3], 4)
print(t[1])
t[1].append(5)
print(t)

for item in t:
    print(item)

