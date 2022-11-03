def is_that_number(mes):               # Позволяет ввести с консоли целое число, возвращая
  print(mes)                           # пользователя ко вводу каждый раз, если ввод не корректен
  val = input('=>  ')
  try:
    return int(val)
  except ValueError:
    print('\033[1;31mЭто не число!\033[0m')
    return is_that_number(mes)

def convert_decimal_to_binary(number):
  rem = ''  
  while number != 0:
    rem = str(rem) + str(number % 2)
    number = number // 2
  return rem[-1::-1]

print('\n'*3)
print('\t\tЗадача 4')
print('*'*60)
print('  Напишите программу, которая будет преобразовывать десятич\nное число в двоичное.\n')
numb_dec  = is_that_number('  Введите целое десятичное число\n')
print(f'число {numb_dec} в двоичной системе = {convert_decimal_to_binary(numb_dec)}')
print('*'*60)
print('\n'*3)