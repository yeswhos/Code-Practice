def validAlphatable(s1, s2):
    # result = list()
    # for i in range(26):
    #     result.append(0)
    # for i in s1:
    #     result[ord(i)] += 1
    #
    l1 = list(s1)
    l2 = list(s2)
    l1.sort()
    l2.sort()
    if l1 == l2:
        return True
    else:
        return False

print(validAlphatable('abcde', 'abced'))

