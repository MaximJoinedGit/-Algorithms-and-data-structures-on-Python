# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

from random import randint

# Массив и два значения для минимальных значений - для самого минимального и второго после него.
nums = [randint(1, 100) for _ in range(10)]
min_num = min_after_min = None

for num in nums:
    if min_num is None:
        min_num = num
    elif num <= min_num:
        min_after_min = min_num
        min_num = num
    elif min_after_min is None or num < min_after_min:
        min_after_min = num

print(f'В исходном массиве {nums} минимальный элемент {min_num}, а второй минимальный {min_after_min}.')
