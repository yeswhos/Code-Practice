N = 332
res = list(str(N))
res.sort()
while str(N) != "".join(res):
    N -= 1
    res = list(str(N))
    res.sort()
    print(N)
print("".join(res))