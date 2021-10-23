def season_check(month):
    """
    please inout number of month
    months 1,2,12 - winter
    months 3,4,5 - spring
    months 6,7,8 - summer
    months 9,10,11 -fall
    """
    if 9 <= month <= 11:
        return 'fall'
    elif 3 <= month <= 5:
        return 'spring'
    elif 6 <= month <= 8:
        return 'summer'
    else:
        return 'winter'


print(season_check(int(input('input month'))))
