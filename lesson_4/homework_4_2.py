# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте
# его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
#
# Вывод:
# Функция sieve() имеет квадратичную сложность алгоритма, в то время как функция prime() имеет экспоненциальную.
# Для решения задачи, безусловно, лучше использовать функцию, работающую на алгоритме решета Эратосфена.

import cProfile


def sieve(pos):
    length = 1

    while True:
        length *= 2
        sie = [i for i in range(pos * length)]
        sie[1] = 0

        for i in range(2, pos * length):
            if sie[i] != 0:
                j = i * 2
                while j < pos * length:
                    sie[j] = 0
                    j += i
        result = [i for i in sie if i != 0]
        if len(result) > pos - 1:
            break

    return result[pos - 1]


# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_2" "homework_4_2.sieve(10)"
# 1000 loops, best of 5: 40 usec per loop
#
# cProfile.run('sieve(10)')
#           10 function calls in 0.000 seconds
#         1    0.000    0.000    0.000    0.000 homework_4_2.py:12(sieve)
#
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_2" "homework_4_2.sieve(25)"
# 1000 loops, best of 5: 106 usec per loop
#
# cProfile.run('sieve(25)')
#           10 function calls in 0.000 seconds
#         1    0.000    0.000    0.000    0.000 homework_4_2.py:12(sieve)
#
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_2" "homework_4_2.sieve(50)"
# 1000 loops, best of 5: 583 usec per loop
#
# cProfile.run('sieve(50)')
#           13 function calls in 0.001 seconds
#         1    0.001    0.001    0.001    0.001 homework_4_2.py:12(sieve)
#
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_2" "homework_4_2.sieve(100)"
# 1000 loops, best of 5: 1.38 msec per loop
#
# cProfile.run('sieve(100)')
#           13 function calls in 0.003 seconds
#         1    0.003    0.003    0.003    0.003 homework_4_2.py:12(sieve)
#
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_2" "homework_4_2.sieve(250)"
# 1000 loops, best of 5: 3.7 msec per loop
#
# cProfile.run('sieve(250)')
#           13 function calls in 0.003 seconds
#         1    0.003    0.003    0.003    0.003 homework_4_2.py:12(sieve)
#
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_2" "homework_4_2.sieve(500)"
# 1000 loops, best of 5: 7.88 msec per loop
#
# cProfile.run('sieve(500)')
#           13 function calls in 0.007 seconds
#         1    0.006    0.006    0.007    0.007 homework_4_2.py:12(sieve)

def prime(pos):
    result = [2]
    num = 2

    while len(result) <= pos - 1:
        num += 1
        div = 1
        times = 0

        if num % 2:
            while div <= num ** 0.5:
                if not num % div:
                    div += 1
                    times += 1
                else:
                    div += 1
            if times <= 1:
                result.append(num)

    return result[pos - 1]

# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_2" "homework_4_2.prime(10)"
# 1000 loops, best of 5: 48.1 usec per loop
#
# cProfile.run('prime(10)')
#           41 function calls in 0.000 seconds
#         1    0.000    0.000    0.000    0.000 homework_4_2.py:81(prime)
#
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_2" "homework_4_2.prime(25)"
# 1000 loops, best of 5: 262 usec per loop
#
# cProfile.run('prime(25)')
#           124 function calls in 0.000 seconds
#         1    0.000    0.000    0.000    0.000 homework_4_2.py:81(prime)
#
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_2" "homework_4_2.prime(50)"
# 1000 loops, best of 5: 863 usec per loop
#
# cProfile.run('prime(50)')
#           281 function calls in 0.002 seconds
#         1    0.001    0.001    0.002    0.002 homework_4_2.py:81(prime)
#
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_2" "homework_4_2.prime(100)"
# 1000 loops, best of 5: 2.95 msec per loop
#
# cProfile.run('prime(100)')
#           643 function calls in 0.003 seconds
#         1    0.003    0.003    0.003    0.003 homework_4_2.py:81(prime)
#
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_2" "homework_4_2.prime(250)"
# 1000 loops, best of 5: 13.9 msec per loop
#
# cProfile.run('prime(250)')
#           1835 function calls in 0.024 seconds
#         1    0.023    0.023    0.024    0.024 homework_4_2.py:81(prime)
#
# C:\Users\Maxim\Documents\GeekBrains\1 четверть. Алгоритмы и структуры данных на Python\Tasks\lesson_4>
# python -m timeit -n 1000 -s "import homework_4_2" "homework_4_2.prime(500)"
# 1000 loops, best of 5: 46.7 msec per loop
#
# cProfile.run('prime(500)')
#           4073 function calls in 0.045 seconds
# 1    0.043    0.043    0.044    0.044 homework_4_2.py:81(prime)
