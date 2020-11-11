def isNumber(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

while True:
    try:
        n = int(input())
        if n <= 1000 or n >= 2000:
            return 0
        else:
            for i in range(n - 1, -1, -1):
                if isNumber(i):
                    return i
    except:
        break