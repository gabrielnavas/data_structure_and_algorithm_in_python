num_integer = input('put the number integer:  ')
if not num_integer.isnumeric():
  print('this number is not integer')


hour_now = int(input('put hour now: '))
minute_now = int(input('put minute now: '))

output_hour = f'{hour_now}:{minute_now}'

if 6 <= hour_now < 12:
  print(f'good morning {output_hour}')
elif 12 <= hour_now < 18:
  print(f'good afternoon {output_hour}')
elif 18 <= hour_now < 0:
  print(f'good evening {output_hour}')
else:
  print(f'good night {output_hour}')


my_name = input('put your name: ')

if len(my_name) <= 4:
  print('your name is short')
elif len(my_name) in [5, 6]:
  print('your name is normal')
elif len(my_name) > 6:
  print('your name is large')