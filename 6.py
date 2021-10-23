def list_calc(number, start_number, stop_number):
    for i in range(start_number, stop_number + 1):
        print(number, ' * ', i, ' = ', number * i)


numbers = input('Введите числа для таблицы умножения числа M в диапазоне от числа a до числа b, разделитель пробел>>').split()
list_calc(number=int(numbers[0]), start_number=int(numbers[1]), stop_number=int(numbers[2]))