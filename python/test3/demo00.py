# n = str(input())
# lo = int(input())
# hi = int(input())
# n = "I am a developer."
# lo = 1
# hi = 2
n = "  hello world!"
lo = 0
hi = 1
li = []
# n = "I am a   developer."
# lo = 0
# hi = 3
# n = "Hello!"
# lo = 0
# hi = 3
for item in n.split(" "):
    if item != "":
        li.append(item)

res = li[lo:hi + 1]
print(res)
res = res[::-1]
if hi > len(li):
    res = ["EMPTY"]
    li = []
for item in li[:lo]:
    print(str(item), end = " ")
for item in res:
    print(str(item), end = " ")
for item in li[hi + 1:]:
    print(str(item), end=" ")

# print(li[:lo])
# print(res)
# print(li[hi + 1:])
