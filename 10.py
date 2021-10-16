numbers = [1, 2, 3, 4, 5, 6, 7]
max_num = max(numbers)
min_num = min(numbers)
print(numbers, max_num, min_num)
for _ in range(len(numbers)):
    if numbers[_] == min_num:
        numbers[_] = max_num
    elif numbers[_] == max_num:
        numbers[_] = min_num
print(numbers)
