while True:
    try:
        s = list(input())[2:]
        n = len(s)
        res = 0
        i = 0
        dic = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
        for item in s[::-1]:
            if item.isnumeric():
                num = int(item)
            elif item.isalpha():
                num = dic[item]
            res = num * 16 ** i + res
            i += 1
        print(res)
    except:
        break