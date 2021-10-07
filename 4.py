number = input('please input numbers with delimeter space" " number>>').split()
for i in range(len(number)):
    if (float(number[i]) % 2) != 0:
        print(number[i])