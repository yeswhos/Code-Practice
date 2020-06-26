file_read = open("D:\GitR\Code-Practice\README.md")
file_write = open("D:\python_a.md", "w")

while True:
    text = file_read.readline()
    if not text:
        break
    file_write.write(text)

file_read.close()
file_write.close()