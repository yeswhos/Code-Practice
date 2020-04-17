#去空白

str_1 = ["    abc", "\t\n efg", "higkl \n"]

for str in str_1:
    print("|%s|" % str.strip().center(10, " "))

    #print(str_1)
    str = str.split()
    print(' '.join(str))