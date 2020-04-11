list1 = [1, 2, 3, 3, 4, 5, 5]
temp = []
for each in list1:
    if each not in temp:
        temp.append(each)
print('temp', temp)

list1 = list(set(list1))
print('set', list1)

set1 = set(list1)
print(len(set1))
set1.add(6)
set1.remove(4)
print(set1)