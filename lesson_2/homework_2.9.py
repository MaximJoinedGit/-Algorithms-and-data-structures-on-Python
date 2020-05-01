# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

n = int(input('Сколько чисел вы будете вводить? '))

# Вводим две переменные для максимального значения суммы цифр числа и для этого числа
max_sum = 0
max_num = 0

# Проходим циклом по каждому числу и в случае, если сумма цифр числа в цикле была больше максимального,
# присваиваем максимальному текущее значение
for i in range(n):
    num = int(input(f'Введите {i + 1}-е число: '))
    temp_sum = 0
    num_copy = num
    while num_copy:
        temp_num = num_copy % 10
        num_copy //= 10
        temp_sum += temp_num
    if temp_sum > max_sum:
        max_sum = temp_sum
        max_num = num
print(f'Сумма цифр числа была больше у числа {max_num}\n'
      f'Сумма его цифр равна {max_sum}')
