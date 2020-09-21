#字符串索引
s = 'hello'
print("index", s.index('lo'))
print("rindex", s.rindex('lo'))
print("find", s.find('lo'))
print("rfind", s.rfind('lo'))

#if string is not found then return -1
print('not found', s.find('k'))


#字符串大小写转换
s = 'hello world'
print('all lower', s.lower())
print('all upper', s.upper())
print('lower turn to upper, upper turn to lower', s.swapcase())
print('upper the very first letter', s.capitalize())
print('upper every first letter', s.title())

#居中，左对齐，右对齐
print(s.center(20, '*'))
print(s.ljust(20, '*'))
print(s.rjust(20))
print(s.zfill(20))

#字符串的分割
s_1 = 'hello-world'
print(s.split())
print(s_1.split(sep = '|'))
print(s_1.split(sep = '|', maxsplit= 1))
#rsplit是从右边开始分割，都是一样的用法
