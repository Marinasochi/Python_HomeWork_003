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
print('\t\tЗадача 2')
print('*'*60)
print('  Напишите программу, которая найдёт произведение пар чисел \nсписка. Парой считаем первый и последний элемент, второй и пред-\nпоследний и т.д.')
set = input_set('  Введите через пробел элементы списка – числа. Для оконча-\nния ввода нажмите "Enter"\n ')
a = round(len(set) / 2 + 0.5)
new_set = [a*b for a, b in zip(set[0: a], set[-1::-1])]
print(new_set)
print('*'*60)
print('\n'*3)