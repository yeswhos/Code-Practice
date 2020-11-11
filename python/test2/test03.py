
# n = str(input())
# m = int(input())
n = "我ABC汉DEF"
m = 6
count = 0
if n[:m] >= u'\u4e00' and n[:m] <=u'\u9fa5':
    count += 1
print(n[:m - (2 * count)])
