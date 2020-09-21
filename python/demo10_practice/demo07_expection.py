# try:
#     a = 1
#     b = 0
#     result = a / b
# except ZeroDivisionError:
#     print("expected error")

#valueerror baseexception

# try:
#     n1 = int(input())
#     n2 = int(input())
#     result = n1 / n2
# except BaseException as e:
#     print(e)
# else:
#     print(result)
# finally:
#     print(result + "666")

import traceback

try:
    result = 1 / 0
except:
    traceback.print_exc()


