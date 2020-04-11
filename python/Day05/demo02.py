f = open('demo.txt')
boy = []
girl = []
for each_line in f:
    if each_line[:5] != '=====':
        (role, spoken) = each_line.split(":", 1)
        if role == '小甲鱼':
            boy.append(each_line)
        else:
            girl.append(each_line)
print("boy", boy)
print("girl", girl)