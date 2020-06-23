def inputPass():
    password = input("input integer")
    if(len(password) > 8):
        return password
    print("exception")
    ex = Exception("主动异常")
    raise ex
try:
    print(inputPass())
except Exception as result:
    print(result)