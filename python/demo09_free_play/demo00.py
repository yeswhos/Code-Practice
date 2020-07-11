#如果a + b + c == 1000, a ^ 2 + b ^ 2 = c ^ 2，求所有abc可能的组合
import math
def combination(num):
    for a in range(0, num + 1):
        for b in range(0, num + 1):
            for c in range(0, num + 1):
                if (math.pow(a, 2) + math.pow(b, 2) + math.pow(c, 2) == num):
                    print(a, "\t", b,  "\t", c)

combination(1000)
