def huiwen(string):
    list1 = list(string)
    list2 = list(reversed(string))
    if(list1 == list2):
        print("是回文")
    else:
        print("不是回文")

a = "上海自来水来自海上"
huiwen(a)