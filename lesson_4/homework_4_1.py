# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
# первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом
# (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.
#
# Задача: Определить, какое число в массиве встречается чаще всего.
#
# first_way() делает из массива множество, затем для каждого числа в множестве считает количество вхождений в массив
# через метод .count
# second_way() сначала сортирует массив, затем в цикле сравнивает значения и считает сколько раз совпали значения
# i-го элемента и элемента i + 1. Как только значения не совпали счетчик обнуляется.
# Лучшее значение переходит в переменную.
# third_way() считает через словарь (ключи и значения).
#
# Вывод: для решения этой задачи были использованы три варианта решения. Все три варианта имели
# линейную сложность алгоритма. Третий вариант выдает решение на 20% дольше первых двух, а первый вариант дает результат
# чуть быстрее второго, поэтому использование первого варианта решения лучше всего подходит для решения данной задачи.
# (Функция first_way())

from random import randint
import cProfile


def first_way(iters):
    nums = [randint(1, 10) for _ in range(iters)]
    counter = max_num = 0
    for num in set(nums):
        temp_counter = nums.count(num)
        if temp_counter > counter:
            max_num = num
            counter = temp_counter
    return max_num


# first_way(10)
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_1" "homework_4_1.first_way(10)"
# 1000 loops, best of 5: 25.3 usec per loop
#
# cProfile.run('first_way(10)')
#           66 function calls in 0.000 seconds
#         1    0.000    0.000    0.000    0.000 homework_4_1.py:7(first_way)
#
# first_way(50)
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_1" "homework_4_1.first_way(50)"
# 1000 loops, best of 5: 124 usec per loop
#
# cProfile.run('first_way(50)')
#           300 function calls in 0.001 seconds
#         1    0.000    0.000    0.001    0.001 homework_4_1.py:7(first_way)
#
# first_way(100)
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_1" "homework_4_1.first_way(100)"
# 1000 loops, best of 5: 231 usec per loop
#
# cProfile.run('first_way(100)')
#           553 function calls in 0.001 seconds
#         1    0.000    0.000    0.001    0.001 homework_4_1.py:7(first_way)
#
# first_way(500)
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_1" "homework_4_1.first_way(500)"
# 1000 loops, best of 5: 1.28 msec per loop
#
# cProfile.run('first_way(500)')
#           2848 function calls in 0.004 seconds
#         1    0.000    0.000    0.004    0.004 homework_4_1.py:7(first_way)
#
# first_way(1000)
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_1" "homework_4_1.first_way(1000)"
# 1000 loops, best of 5: 2.49 msec per loop
#
# cProfile.run('first_way(1000)')
#           5622 function calls in 0.009 seconds
#         1    0.000    0.000    0.009    0.009 homework_4_1.py:7(first_way)
#
# first_way(5000)
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_1" "homework_4_1.first_way(5000)"
# 1000 loops, best of 5: 12.2 msec per loop
#
# cProfile.run('first_way(5000)')
#           28050 function calls in 0.051 seconds
#         1    0.000    0.000    0.051    0.051 homework_4_1.py:7(first_way)

def second_way(iters):
    nums = [randint(1, 10) for _ in range(iters)]
    count = 1
    max_count = max_num = 0
    nums = sorted(nums)
    for num in range(len(nums) - 1):
        if nums[num] == nums[num + 1]:
            count += 1
        else:
            if count > max_count:
                max_count = count
                max_num = nums[num]
            count = 1
    return max_num


# second_way(10)
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_1" "homework_4_1.second_way(10)"
# 1000 loops, best of 5: 25.9 usec per loop
#
# cProfile.run('second_way(10)')
#           59 function calls in 0.000 seconds
#         1    0.000    0.000    0.000    0.000 homework_4_1.py:72(second_way)
#
# second_way(50)
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_1" "homework_4_1.second_way(50)"
# 1000 loops, best of 5: 127 usec per loop
#
# cProfile.run('second_way(50)')
#           280 function calls in 0.000 seconds
#         1    0.000    0.000    0.000    0.000 homework_4_1.py:72(second_way)
#
# second_way(100)
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_1" "homework_4_1.second_way(100)"
# 1000 loops, best of 5: 249 usec per loop
#
# cProfile.run('second_way(100)')
#           564 function calls in 0.001 seconds
#         1    0.000    0.000    0.001    0.001 homework_4_1.py:72(second_way)
#
# second_way(500)
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_1" "homework_4_1.second_way(500)"
# 1000 loops, best of 5: 1.31 msec per loop
#
# cProfile.run('second_way(500)')
#           2835 function calls in 0.003 seconds
#         1    0.000    0.000    0.003    0.003 homework_4_1.py:72(second_way)
#
# second_way(1000)
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_1" "homework_4_1.second_way(1000)"
# 1000 loops, best of 5: 2.7 msec per loop
#
# cProfile.run('second_way(1000)')
#           5642 function calls in 0.006 seconds
#         1    0.001    0.001    0.006    0.006 homework_4_1.py:72(second_way)
#
# second_way(5000)
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_1" "homework_4_1.second_way(5000)"
# 1000 loops, best of 5: 12.9 msec per loop
#
# cProfile.run('second_way(5000)')
#           27917 function calls in 0.027 seconds
#         1    0.002    0.002    0.027    0.027 homework_4_1.py:72(second_way)

def third_way(iters):
    nums = [randint(1, 10) for _ in range(iters)]
    max_num = counter = 0
    dict_nums = dict.fromkeys(set(nums), 0)
    for key in dict_nums:
        for num in nums:
            if key == num:
                dict_nums[key] += 1
        if dict_nums[key] > counter:
            max_num = key
            counter = dict_nums[key]
    return max_num

# third_way(10)
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_1" "homework_4_1.third_way(10)"
# 1000 loops, best of 5: 31.4 usec per loop
#
# cProfile.run('third_way(10)')
#           61 function calls in 0.000 seconds
#         1    0.000    0.000    0.000    0.000 homework_4_1.py:142(third_way)
#
# third_way(50)
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_1" "homework_4_1.third_way(50)"
# 1000 loops, best of 5: 157 usec per loop
#
# cProfile.run('third_way(50)')
#           276 function calls in 0.001 seconds
#         1    0.000    0.000    0.001    0.001 homework_4_1.py:142(third_way)
#
# third_way(100)
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_1" "homework_4_1.third_way(100)"
# 1000 loops, best of 5: 314 usec per loop
#
# cProfile.run('third_way(100)')
#           570 function calls in 0.001 seconds
#         1    0.000    0.000    0.001    0.001 homework_4_1.py:142(third_way)
#
# third_way(500)
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_1" "homework_4_1.third_way(500)"
# 1000 loops, best of 5: 1.58 msec per loop
#
# cProfile.run('third_way(500)')
#           2809 function calls in 0.006 seconds
#         1    0.001    0.001    0.005    0.005 homework_4_1.py:142(third_way)
#
# third_way(1000)
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_1" "homework_4_1.third_way(1000)"
# 1000 loops, best of 5: 3.17 msec per loop
#
# cProfile.run('third_way(1000)')
#           5589 function calls in 0.007 seconds
#         1    0.002    0.002    0.007    0.007 homework_4_1.py:142(third_way)
#
# third_way(5000)
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_1" "homework_4_1.third_way(5000)"
# 1000 loops, best of 5: 16 msec per loop
#
# cProfile.run('third_way(5000)')
#           28087 function calls in 0.037 seconds
#         1    0.005    0.005    0.037    0.037 homework_4_1.py:142(third_way)
