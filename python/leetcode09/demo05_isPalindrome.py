def isPalindrome(s):
    sgood = ""
    for ch in s:
        if (ch.isalnum()):
            #print(ch)
            #sgood = "".join(ch.lower())
            sgood = sgood + ch.lower()
        print(sgood)
    #print(sgood[::-1])
    return sgood == sgood[::-1]
#s = "A man, a plan, a canal: Panama"
#s = "....a...."
s = "race a car"
print(isPalindrome(s))