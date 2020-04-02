def count(*param):
    for i in range(len(param)):
        space = 0
        letter = 0
        num = 0
        other = 0
        for each in param[i]:
            if each.isalpha():
                letter += 1
            elif each.isdigit():
                num += 1
            elif each == " ":
                space += 1
            else:
                other += 1
        print('There are %d string, each of them include %d letter, %d number, %d space and %d other symbol' % (i + 1, letter, num, space, other) )

count("123abcd", "sdfafy98wyh3!")

