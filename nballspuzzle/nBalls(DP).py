# A Dynamic Programming based Python Program for the Ball Dropping Puzzle

# @input: n balls and k floors
# @output: return the minimum number of trials needed in worst case
def ballDrop(n, k):
    # define an array ballFloor[i][j] to hold the minimum number of trials
    # for i balls and j floors in worst case
    ballFloor = [ [0 for j in range(k + 1)] for i in range(n + 1) ]
    #print(ballFloor)

    # if there is 1 floor or there are no floors, then 1 trial or no trials needed
    for i in range(1, n + 1):
        ballFloor[i][0] = 0
        ballFloor[i][1] = 1

    # k trials for 1 ball and k floors
    for j in range(k + 1):
        ballFloor[1][j] = j

    for i in range(2, n + 1):
        for j in range(2, k + 1):
            # assume k is min(min<=k)
            ballFloor[i][j] = k
            # consider all droppings from 1st to kth floor
            # x is the current floor
            for x in range(1, j + 1):
                result = 1 + max(ballFloor[i - 1][x - 1], ballFloor[i][j - x])
                if result < ballFloor[i][j]:
                    ballFloor[i][j] = result
    return ballFloor[n][k]


print(ballDrop(3, 1000))
