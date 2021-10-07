number = input('please input numbers with delimeter space" " number>>').split()
result = 0
start = int(number[0])
end = int(number[1])
if start < end:
    while start <= end:
        result += start
        start += 1
    print('result ', result)
