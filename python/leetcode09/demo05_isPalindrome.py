def isPalindrome(s):
    s = s.replace(" ", "")
    s = s.lower()
    arr = list(s)
    print(arr)
    for i in arr:
        print(i)
        num = ord(i)
        # if(48 <= num <= 57):
        #     continue
        # elif(97 <= num <= 122):
        #     continue
        # else:
        #     arr.remove(i)
        if (num < 48) or (57 < num < 97) or (num > 122):
            arr.remove(i)
    print(arr)
    if (arr == arr[::-1]):
        return True
    else:
        return False

#s = "A man, a plan, a canal: Panama"
s = "....a...."
print(isPalindrome(s))