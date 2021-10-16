list = [1, 2, 3, 4, 5, 6, 7]
summ = 0
product = 1
for i in range(len(list)):
    summ += list[i]
    product *= list[i]
print(summ, product)
