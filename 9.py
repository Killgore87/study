input_slovar = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}


def dic_calc(slovar):
    a = 1
    print(list(slovar.values()))
    for i in list(slovar.values()):
        a *= i
    return a


print(dic_calc(input_slovar))