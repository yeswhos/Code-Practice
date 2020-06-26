file_read = open("D:\GitR\Code-Practice\README.md")
file_write = open("D:\python_a.md", "w")

text = file_read.read()
file_write.write(text)

file_read.close()
file_write.close()

