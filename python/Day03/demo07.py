#递归归
def hui_wen(n, start, end):
    print(n[start], "---", n[end])
    if start > end:
        return 1
    elif (n[start] != n[end]):
        return 0
    else:
        return hui_wen(n, start + 1, end - 1)
a = "123321"
if hui_wen(a, 0, len(a) - 1):
    print("回文")
else:
    print("不是回文")