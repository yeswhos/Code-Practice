deck = [1,2,3,4,4,3,2,1]
deck = sorted(deck)
s = ""
for item in deck:
    s = s + str(item)
print(s)
while "11" in s or "22" in s or "33" in s or "44" in s:
    s = s.replace("11", "")
    s = s.replace("22", "")
    s = s.replace("33", "")
    s = s.replace("44", "")
if s == "":
    print("True")
else:
    print("False")