file = open("D:\GitR\Code-Practice\README.md")

while True:
    text = file.readline()
    if not text:
        break
    print(text)

file.close()