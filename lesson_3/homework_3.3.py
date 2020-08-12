# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint

# Создаем временные переменные для индексов максимального и минимального значения.
nums = [randint(0, 100) for _ in range(10)]
max_num = min_num = 0

# Проходим с помощью цикла по всем элементам списка. Находим максимальное и минимальное значения, их индексы.
for i in range(len(nums) - 1):
    if nums[i + 1] > nums[max_num]:
        max_num = i + 1
    elif nums[i + 1] < nums[min_num]:
        min_num = i + 1

print(f'Массив перед заменой: {nums}')
nums[max_num], nums[min_num] = nums[min_num], nums[max_num]
print(f'Массив после замены: {nums}')
