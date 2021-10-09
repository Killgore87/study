int_cash = 1
int_cash = float(input('please input summ>>'))
year = 1
year = int(input('please input years>>'))
for i in range(1, year + 1):
    int_cash = int_cash + (int_cash / 100 * 11.5)
print('summ at the end', int_cash)
