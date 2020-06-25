file = open("D:\GitR\Code-Practice\README.md")

text = file.read()
print(len(text))
print("-" * 50)
text = file.read()
print(len(text))
file.close()