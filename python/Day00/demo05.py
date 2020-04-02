#100以内被3整除的数
print(list(filter(lambda x : not(x % 3) , range(1, 100))))