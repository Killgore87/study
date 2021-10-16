numbers = input('please input numbers with delimeter space" " number>>').split()
numbers = [_ for _ in numbers if numbers.count(_) >= 2]
print(list(set(numbers)))