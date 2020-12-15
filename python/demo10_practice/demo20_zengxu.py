N = 322

num = list(str(N))
max_num = -float("inf")
begin = 0
is_result = True
for i in range(1, len(num)):
    nums = int(num[i])
    pre_num = int(num[i - 1])
    if pre_num > max_num:
        max_num = pre_num
        begin = i - 1
    if pre_num > nums:
        is_result = False
        break

if is_result:
    print(N)
else:
    num[begin] = str(int(num[begin]) - 1)
    for i in range(begin + 1, len(num)):
        num[i] = "9"
    print("".join(num))
