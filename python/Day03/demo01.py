#数单词数量
list1 = ['A child in a pink dress is climbing up a set of stairs in an entry way .', 'A girl going into a wooden building .', 'A little girl climbing into a wooden playhouse .']

counts = {}#创建一个空的字典
for i in range(0, 3):
    str = "".join(list1[i])
    str = str.lower()
    print(str)
    words = str.split()
    
    #print(words)
    for word in words:

        counts[word] = counts.get(word,0)+1
    #print(counts)
    items = list(counts.items())#将字典中的每对键值对看做一个元素存入items列表中
    # items.sort(key=lambda x:x[1],reverse=True)
    #根据lambda表达式来进行排序 在这里是根据数字来排序
list2 = []
for i in range(len(items)):
    word,count = items[i]
    if (count > 1) & (word != '.') & (word != ','):
        list2.append(word)
            
    
    print(word, count)

print(list2)
