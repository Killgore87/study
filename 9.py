numbers = [1, 20, 3, 4, 5, 6, 7, 20, 555, 5, 20, 'ss', 'ss']
numbers = [_ for _ in numbers if numbers.count(_) >= 2]
print(list(set(numbers)))
