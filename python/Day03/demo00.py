#数字母数量
list = [['A', 'child', 'in', 'a', 'pink', 'dress', 'is', 'climbing', 'up', 'a', 'set', 'of', 'stairs', 'in', 'an', 'entry', 'way', '.'], ['A', 'girl', 'going', 'into', 'a', 'wooden', 'building', '.'], ['A', 'little', 'girl', 'climbing', 'into', 'a', 'wooden', 'playhouse', '.']]
mydict={}
for j in range(0, 4):
    str = "".join(list[j])
    for i in str:
        if i in mydict:
            mydict[i]+=1
        else :
            mydict[i]=1
    for key,value in mydict.items():
        print(key,value)
