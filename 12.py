number = input('please input number>>')
result = 0
for n in range(len(list(number))):
    if list(number)[n] != '.' and list(number)[n] != ',' and list(number)[n] != '-':
        if result < int(list(number)[n]):
            result = int(list(number)[n])
print('result ', result)
