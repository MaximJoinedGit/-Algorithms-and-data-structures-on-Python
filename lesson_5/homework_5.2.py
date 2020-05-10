# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
#
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

# Два словаря для перевода в шестнадцатеричную систему и наоборот.
hex_nums = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
            'C': 12, 'D': 13, 'E': 14, 'F': 15}
oct_nums = {v: k for k, v in hex_nums.items()}


def check_input(text: str):
    """
    Функция проверки введенного шестнадцатеричного числа на валидность.
    """
    number = None
    while not number:
        try:
            number = list(input(text))
            for elem in range(len(number)):

                # Проверка на регистр, перевод в верхний регистр.
                if number[elem].isalpha():
                    number[elem] = number[elem].upper()

                # Проверка на валидность. Если числа или буквы нет в словаре, то программа вызывает ValueError и
                # просит ввести значение заново.
                if number[elem] not in hex_nums:
                    number = None
                    raise ValueError
        except ValueError:
            print('Введено неправильное число в шестнадцатеричном виде. Попробуйте ввести снова.')
    return number


def hex_sum(first: list, second: list):
    """
    Функция сложения шестнадцатеричных чисел.
    """

    # Переводим введенные значения в очередь из модуля Collections.
    first = deque([hex_nums[_] for _ in first])
    second = deque([hex_nums[_] for _ in second])

    # Уравниваем длины массивов при необходимости.
    while not len(first) == len(second):
        first.appendleft(0) if len(first) < len(second) else second.appendleft(0)

    # Складываем значения и добавляем в массив слева нулевое значение.
    result = deque(map(lambda x, y: x + y, first, second))
    result.appendleft(0)

    # Если полученное число в массиве больше 16, то остается только остаток от деления,
    # а значение целочисленного деления суммируется к следующему элементу.
    for i in range(1, len(result)):
        if result[-i] > 15:
            result[-i - 1] += result[-i] // 16
            result[-i] %= 16

    # Удаляем нулевое значение слева, если оно осталось нулевым и выводим результат.
    result.remove(0) if result[0] == 0 else result
    return ''.join([oct_nums[_] for _ in result])


def hex_mul(first: list, second: list):
    """
    Функция умножения шестнадцатеричных чисел.
    """

    # Переводим введенные значения в очередь из модуля Collections.
    first = deque([hex_nums[_] for _ in first])
    second = deque([hex_nums[_] for _ in second])

    result = deque()
    for i in range(1, len(second) + 1):

        # Умножаем весь первый массив на каждый элемент второго массива отдельно.
        temp_result = deque(map(lambda x: x * second[-i], first))

        # При каждом следующем умножении мы смещаем массив на один знак.
        while not len(temp_result) == len(first) + i - 1:
            temp_result.append(0) if i > 1 else temp_result.appendleft(0)

        # Делаем длины массивов равными и сладываем массивы.
        while not len(result) == len(temp_result):
            result.appendleft(0)
        result = deque(map(lambda x, y: x + y, result, temp_result))

    # Если полученное число в массиве больше 16, то остается только остаток от деления,
    # а значение целочисленного деления суммируется к следующему элементу.
    result.appendleft(0)
    for j in range(1, len(result)):
        if result[-j] > 15:
            result[-j - 1] += result[-j] // 16
            result[-j] %= 16

    # Удаляем нулевое значение слева, если оно осталось нулевым и выводим результат.
    result.remove(0) if result[0] == 0 else result
    return ''.join([oct_nums[_] for _ in result])


# Реализация интерфейса калькулятора.
user_input = True
while user_input:
    action = input('Введите знак операции + или *. Введите 0 для выхода.\n')
    if action == '+':
        print(hex_sum(check_input('Введите первое число в 16-чной системе: '),
                      check_input('Введите второе число в 16-чной системе: ')))
    elif action == '*':
        print(hex_mul(check_input('Введите первое число в 16-чной системе: '),
                      check_input('Введите второе число в 16-чной системе: ')))
    elif action == '0':
        break
    else:
        print(f'{action} - Неизвестная команда. Повторите ввод.')
