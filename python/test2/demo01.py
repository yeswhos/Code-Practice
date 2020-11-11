# n = str(input())
#n = "3[a]2[bc]"
n = "100[abc]"
a = []
times = 0
res = ""
for s in n:
    if s.isdigit():
        times = times + int(s)
    elif s == "[":
        a.append((res, times))
        res = ""
        times = 0
    elif s == "]":
        top = a.pop()
        res = top[0] + res * top[1]
    else:
        res += s
print(res)