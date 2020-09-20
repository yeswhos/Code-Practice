#字典的创建
score = {'jack' : 18, 'rose' : 17}
#print(score)

scores = dict(name = 'jack', age = 18)
#rint(scores)

#字典的查找
# print(score['jack'])
# print(score.get('jack'))
# print(score.get('jerry'))
# #不存在时，返回这个值
# print(score.get('jaack', 99))

#字典的视图操作，keys，values，items. 健，值，键值对
# print(score.keys())
# print(score.values())
# print(score.items())
# #tuple
# print(list(score.items()))

#字典的遍历
for item in score:
    print("key", item, '\n')
    print("value", score.get(item), '\n')
    print("value", score[item], '\n')

#用列表生成字典
name = ['jack', 'rose']
age = [18, 17]
dicts = {name:age   for name, age in zip(name, age)}
print(dicts)