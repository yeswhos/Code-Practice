# def fib(num):
#     count, a, b = 0, 0, 1
#     while count < num:
#         print(b)
#         a, b = b, a + b
#         count = count + 1
#     return 'done'
#
# fib(10)

def fib_gen(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'
a = fib_gen(10)
for i in a:
    print(i)