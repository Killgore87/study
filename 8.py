first = int(input('Pervoe chislo>>'))
second = int(input('Vtoroe chislo>>'))
if first < second:
    while first <= second:
        print(first)
        first += 1
elif first > second:
    while first >= second:
        print(first)
        first -= 1
