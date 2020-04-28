# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

first, second, third = input('Введите три числа через пробел: ').split()
first, second, third = int(first), int(second), int(third)

# Определяем наибольшее число и далее работаем с оставшимися двумя.
if not first > second:
    first, second = second, first
if not first > third:
    first, third = third, first

# Определяем наименьшее число, которое и будет средним из трех заданных.
if second > third:
    print(f'Среднее число - {second}')
else:
    print(f'Среднее число - {third}')
