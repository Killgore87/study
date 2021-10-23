numbers = input('please input numbers with delimeter space" " number>>').split()
def list_calc(number, size):
    result_list = []
    result_number = 0
    if int(size) != 1:
        for i in range(1, int(size) + 1):
            result_list.append(number * i)
        for a in result_list:
            result_number += int(a)
        return result_number
    else:
        return number
print(list_calc(number=numbers[0], size=numbers[1]))


