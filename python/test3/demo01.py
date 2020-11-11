n = [1,0,0,0,0,1,0,0,1,0,1]
res = 0
b = len(n)
li = []
a = []
for i in range(len(n)):
    if n[i] == 1:
        li.append(i)
for i in range(len(n)):
    if n[i] == 0:
        for num in li:
            temp = abs(i - num)
            if temp < b:
                b = temp
        a.append(b)
        b = len(n)
print(max(a))