number_1 = int(input('please input number_1>>'))
number_2 = int(input('please input number_2>>'))
number_3 = int(input('please input number to compare>>'))
if number_1 < number_3 < number_2 or number_2 < number_3 < number_1:
    print('true')
else:
    print('false')