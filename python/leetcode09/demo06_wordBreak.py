def wordBreak(s, wordDict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(n):
        for j in range(i + 1, n + 1):
            if dp[i] and s[i : j] in wordDict:
                dp[j] = True
    return dp[-1]

s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))