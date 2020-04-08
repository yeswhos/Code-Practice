#递归归归
list = []
def puzzle(num1):
    if len(list) >= 5:
        print(list)
    else:
        list.append(num1)
        return puzzle(num1 + 2)

puzzle(10)

def puzzle_official(n):
    if n == 1:
        return 10
    else:
        return puzzle_official(n - 1) + 2

print(puzzle_official(5))