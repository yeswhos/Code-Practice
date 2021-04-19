s = "AACTGTGCACGACCTGA"
n = 5
res = 0
store = 0
for i in range(0, len(s) - n + 1):
    ratio = s.count("C", i, i + n) + s.count("G", i, i + n)
    if ratio > res:
        res = ratio
        store = i
print(s[store: store + n])