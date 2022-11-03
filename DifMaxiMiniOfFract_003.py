def input_set(mes):                          # Позволяет ввести список вещественных чисел, 
   try:                                      # произвольной длины, возвращая пользователя к вводу,
     nums = input(mes).split(' ')            # если введено не число.
     str = list(nums)
     mas = [float(x) for x in str]
     print(mas)
     return mas
   except ValueError:
     print('\033[1;31mЭто не число!\033[0m')
     return input_set(mes)

print('\n'*3)
print('\t\tЗадача 3')
print('*'*60)
print('  Задайте список из вещественных чисел. Напишите программу,\nкоторая найдёт разницу между максимальным и минимальным зна-\nчением дробной части элементов.\n')
series  = input_set('  Введите через пробел элемениты списка, целые числа. Для\nокончания ввода нажмите "Enter"\n')
new_series = [round(abs(i)%1, 3) for i in series if i%1 != 0]
print(f'Новый список: {new_series}')
print(f'Разница между макс-ым и мин-ым эл-ми нового списка:\n {max(new_series)} - {min(new_series)} = {max(new_series) - min(new_series)}')
print('*'*60)
print('\n'*3)