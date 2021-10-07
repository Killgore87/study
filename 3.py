number = float(input('number>>'))
measure = input('input farinhate or celsius measure, format = C or F >>')
if measure == 'C' or measure == 'c':
    result = (number * 1.8) + 32
    print('result in F', result)
else:
    result = (number - 32) / 1.8
    print('result in C', result)