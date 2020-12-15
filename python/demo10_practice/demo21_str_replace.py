s = "We are happy."
n = list(s).count(" ")
s = s.replace(" ", "%20", n)
print(s)