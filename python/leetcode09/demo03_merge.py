def merge (nums1, m, nums2, n):
    length = len(nums1)
    nums1 = nums1 + nums2
    for i in range(length - m):
        nums1.remove(0)
    nums1.sort()
    print(nums1)

nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m, n = 3, 3
merge(nums1, m, nums2, n)
