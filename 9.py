n = int(input('Input size of diamond>>'))
for i in range(1, n):
    for a1 in range(n - i):
        print(' ', end='')
    for a2 in range((i * 2) - 1):
        print('*', end='')
    print()
for i in reversed(range(1, n-1)):
    for a1 in range(n - i):
        print(' ', end='')
    for a2 in range((i * 2) - 1):
        print('*', end='')
    print()
