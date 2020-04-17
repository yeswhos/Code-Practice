#对齐

str = ["abc", "efg", "higkl"]

for str_1 in str:
    # print(str_1.center(10))
    # print("-----------------------------------------")
    # print("|%s|" % str_1.center(10, " "))
    print("|%s|" % str_1.ljust(10, " "))
    print("|%s|" % str_1.rjust(10, " "))