# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint

nums = [randint(1, 100) for _ in range(10)]
max_num = min_num = 0
sum_between = 0

# Действия, аналогичные действиям в задании 3.
for i in range(len(nums) - 1):
    if nums[i + 1] > nums[max_num]:
        max_num = i + 1
    elif nums[i + 1] < nums[min_num]:
        min_num = i + 1

# Два варианта решения задачи в зависимости от взаимного расположения максимального и минимального элемента.
if max_num > min_num:
    for elem in range(min_num + 1, max_num):
        sum_between += nums[elem]
else:
    for elem in range(max_num + 1, min_num):
        sum_between += nums[elem]

print(f'В массиве {nums} сумма элементов, находящаяся между минимальным и максимальным равна {sum_between}.')
