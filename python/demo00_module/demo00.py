def print_line(char, time):
    '''
    打印单行分割线
    :param char: 分割字符
    :param time: 重复次数
    '''
    print(char * time)

def print_lines(char, time):
    '''打印多行分割线

    :param char: 分割字符
    :param time:重复次数
    :return:
    '''
    row = 0
    while row < 5:
        print_line(char, time)
        row += 1

name = 'Fanhui'