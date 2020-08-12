# Задача. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
# со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
# (помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.

# Вывод.
# Для проверки я решил взять массив, который задан в примере.
# Количество переменных и память:
# 1. 4 переменных и 284 байта.
# 2. 3 переменных и 270 байт.
# 3. 5 переменных и 312 байт.

# Довольно очевидный вывод - второй вариант решения короче, используется меньше переменных и меньше памяти.

# Версия Python и система
# 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)] win32


from sys import getsizeof

all_nums = [8, 3, 15, 6, 4, 2]

# Вариант №1.

# *********************************************************************************************************************
# Функции и переменные, которые мы анализировали на количество занимаемой памяти:
# all_nums, even_nums_one, getsizeof, i
# Количество памяти, которое занял алгоритм: 284 байт
# *********************************************************************************************************************

# even_nums_one = list()
# for i in range(len(all_nums)):
#     if not all_nums[i] % 2:
#         even_nums_one.append(i)

# # Вариант №2.

# *********************************************************************************************************************
# Функции и переменные, которые мы анализировали на количество занимаемой памяти:
# all_nums, even_nums_two, getsizeof
# Количество памяти, которое занял алгоритм: 270 байт
# *********************************************************************************************************************

# even_nums_two = [num for num in range(len(all_nums)) if not all_nums[num] % 2]

# Вариант №3.

# *********************************************************************************************************************
# Функции и переменные, которые мы анализировали на количество занимаемой памяти:
# all_nums, copy, even_nums_three, getsizeof, index
# Количество памяти, которое занял алгоритм: 312 байт
# *********************************************************************************************************************

# copy = all_nums.copy()
# even_nums_three = list()
# index = 0
# while copy:
#     if not copy[0] % 2:
#         even_nums_three.append(index)
#     copy.pop(0)
#     index += 1

vars_before_func = dir().copy()


def show_size(x, level=0):
    # print('\t' * level, f'type={x.__class__}, size={getsizeof(x)}, object={x}')
    spam = 0

    if hasattr(x, '__iter__'):
        if hasattr(x, '__items__'):
            for xx in x.items():
                show_size(xx, level + 1)
                spam += getsizeof(xx)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)
                spam += getsizeof(xx)

    return spam + getsizeof(x)


if __name__ == '__main__':
    # assert even_nums_one == even_nums_two == even_nums_three
    total_size = 0
    for elem in vars_before_func:
        total_size += show_size(locals()[str(elem)]) if not elem[0] == '_' else False
    print(f"Функции и переменные, которые мы анализировали на количество занимаемой памяти:\n"
          f"{', '.join([var for var in vars_before_func if not var[0] == '_'])}")
    print(f'Количество памяти, которое занял алгоритм: {total_size} байт')
