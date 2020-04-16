str_1 = 'hello world'

print('判断开始', str_1.startswith("h"))
print('判断结束', str_1.endswith("world"))

print('查找', str_1.find("world"))
print('查找', str_1.index("world"))

print('代替', str_1.replace("world", "python"), str_1)