# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если
# введено число 3486, надо вывести 6843.

num = int(input('Введите любое целое число: '))


def reverse_number(number):
    if number:
        print(number % 10, end='')
        reverse_number(number // 10)


print(f'Обратное число')
reverse_number(num)
