for i in range(0, 5):
    if i == 0 or i == 4:
        for a in range(0, 22):
            print('*', end='')
        print(' ')
    else:
        for b in range(0, 22):
            if b == 0 or b == 21:
                print('*', end='')
            else:
                print(' ', end='')
        print(' ')