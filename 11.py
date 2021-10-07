number = input('please input numbers with delimeter space" " number>>').split()
result = 1
start = int(number[0])
end = int(number[1])
if start < end:
    while start <= end and start % 2 == 0:
        if start == 0:
           start += 1
        result *= start
        start += 1
    print('result ', result)