first = int(input('first number>>'))
second = int(input('second number>>'))
third = int(input('third number>>'))
fourth = int(input('fourth number>>'))
if 8 >= first > 0 and 8 >= second > 0 and 8 >= third > 0 and 8 >= fourth > 0:
    pass
else:
    print('wrong input')
if (first + second + third + fourth) % 2 == 0:
    print('Same color - YES')
else:
    print('Same color - NO')