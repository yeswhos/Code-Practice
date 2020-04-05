#Test for coursework

# list1 = ['A', 'child', 'in', 'a', 'pink', 'dress', 'is', 'climbing', 'up', 'a', 'set', 'of', 'stairs', 'in', 'an', 'entry', 'way', '.'], ['A', 'girl', 'going', 'into', 'a', 'wooden', 'building', '.'], ['A', 'little', 'girl', 'climbing', 'into', 'a', 'wooden', 'playhouse', '.']
list2 = []
q = 'A child in a pink dress is climbing up a set of stairs in an entry way .'
q1 = 'A girl going into a wooden building .'
# q='hello world god is hello busy'
a=q.split(' ')
f=''.join(a)

a1=q1.split(' ')
f1=''.join(a1)
for i in a:
    b=a.count(i)
    if i not in list2:
        list2.append(i)
for i in a1:
    b=a1.count(i)
    if i in list2:
        b += 1
    if i not in list2:
        list2.append(i)

for k in list2:
    print(k,':',b,end='  ')
