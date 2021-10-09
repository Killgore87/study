import calendar
year = int(input('please input year>>'))
if calendar.monthrange(year, 2)[1] == 29:
    print('leap year')
else:
    print('normal year')