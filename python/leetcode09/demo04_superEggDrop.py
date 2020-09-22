def superEggDrop(K, N):
    memo = {}

    def dp(k, n):
        if (k, n) not in memo:
            if k == 1:
                ans = n
            elif n == 0:
                ans = 0
            else:
                lo = 1
                hi = n
                while (lo + 1 < hi):
                    x = (lo + hi) // 2
                    t1 = dp(k - 1, x - 1)
                    t2 = dp(k, n - x)
                    # 摔碎的情况次数大于没摔碎的
                    if t1 > t2:
                        hi = x
                    elif t1 < t2:
                        lo = x
                    else:
                        lo = hi = x

                ans = 1 + min((max(dp(k - 1, x - 1), dp(k, n - x)))
                            for x in (lo, hi))
            memo[k, n] = ans
        return memo[k, n]

    return dp(K, N)


a = superEggDrop(2, 100)
print(a)
