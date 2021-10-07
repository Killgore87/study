first = int(input('Pervoe chislo>>'))
second = int(input('Vtoroe chislo>>'))
result_first = first % second
result_second = first / second
if first >= second:
   print('Chastnoe', int(result_second))
   if result_first != 0:
      print('Ostatok ', result_first)
else:
   print('Ne delitsya')