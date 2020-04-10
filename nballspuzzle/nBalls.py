
# @input: n balls and k floors
# @output: return minimum number of trials in worst case
def ballDrop(n, k):

    # if there is 1 floor or there are no floors, then 1 trial or no trials needed
    if k == 1 or k == 0:
        return k

    # k trials for 1 ball and k floors
    if n == 1:
        return k
    
    # assume k is min(min<=k)
    min = k

    # consider all droppings from 1st to kth floor
    # x is the current floor
    for x in range(1, k + 1):
        
        result = 1 + max(ballDrop(n - 1, x - 1), ballDrop(n, k - x))  
        if result < min:
            min = result
        
    return min


print(ballDrop(2, 10))
