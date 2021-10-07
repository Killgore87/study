number = input('please input numbers with delimeter space" " number>>').split()
result = 1
input_range = range(int(number[0]), (int(number[1])+1))
for n in input_range:
    if n % 2 == 0 and n != 0:
        result *= n
print('result ', result)
