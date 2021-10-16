list = []
for _ in range(0, 100):
    if _ % 2 == 0:
        list.append(_)
    if len(list) == 45:
        break
print(len(list), list)
