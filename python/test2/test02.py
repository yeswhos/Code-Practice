key, value = "NIHAO", "NI"
dic = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
key = set(list(key))
new_dic = []
res = ""
for item in list(key):
    new_dic.append(item)
for item in dic:
    if item not in new_dic:
        new_dic.append(item)
for item in list(value):
    n = dic.index(item)
    res = res + str(new_dic[n])
print(res)