# a = [1, 2, 3]
# dp = [[0 for _ in range(5)] for _ in range(3)]
# print(dp)
a = [1, 2, 3, 2, 1]
b = [3, 2, 1, 4, 7]
class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        m = len(B)
        res = 0
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, n + 1):
            for j in range(1, m+ 1):
                if(A[i - 1] == B[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1] + 1
                res = max(res, dp[i][j])
        return res

solution = Solution()
c = solution.findLength(a, b)
print(c)

