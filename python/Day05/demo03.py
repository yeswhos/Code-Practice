f = open('demo.txt')
boy = []
girl = []
counter = 0

def file_write(boy, girl):
    boy_file_name = 'boy_' + str(counter) + '.txt'
    girl_file_name = 'girl_' + str(counter) + '.txt'
    boy_file = open(boy_file_name, 'w')
    boy_file.writelines(boy)
    #boy_file.close()
    girl_file = open(girl_file_name, 'w')
    girl_file.writelines(girl)
    # girl_file.close()

for each_line in f:
    if each_line[:6] != '======':
        (role, spoken) = each_line.split(':', 1)
        if role == '小甲鱼':
            boy.append(each_line)
        elif role == '小客服':
            girl.append(each_line)
    else:
        file_write(boy, girl)
        counter += 1
        boy = []
        girl = []
f.close()

