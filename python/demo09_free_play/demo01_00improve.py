#如果a + b + c == 1000, a ^ 2 + b ^ 2 = c ^ 2，求所有abc可能的组合
import math
import time

def combination(num):
    for a in range(0, num + 1):
        for b in range(0, num + 1):

            c = 1000 - a - b
            if (math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)):
                    print(a, "\t", b,  "\t", c)

start_time = time.time()
end_time = time.time()
combination(1000)