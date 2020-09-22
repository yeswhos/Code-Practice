def majorityElement(nums):
    #n = len(nums)
    l1 = list(set(nums))
    l2 = list()
    for i in range(len(l1)):
        l2.append(0)
    for i in l1:
        for j in nums:
            if (i == j):
                l2[l1.index(i)] += 1
    max_number = max(l2)
    result = l2.index(max_number)
    return l1[result]

print(majorityElement([2, 2, 1, 1, 1, 2, 2]))