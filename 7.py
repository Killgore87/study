number = input('please input numbers with delimeter space" " number>>').split()
result = 0
for i in range(len(number)):
    result += float(number[i])
print('result ', result)