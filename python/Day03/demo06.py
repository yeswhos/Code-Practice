#继续递归
result = []
def get_digits(n):
    
    if n > 0:
        result.append(n % 10)
        return get_digits(n // 10)
        #result.append(n)
    result.sort(reverse = False)

get_digits(1234)   
print(result)