def sum_nums(*args):
    result = 0
    for i in args:
        result += i
    # print(result)
    return result

gl_result = sum_nums(1, 2, 3, 4)
print(gl_result)
