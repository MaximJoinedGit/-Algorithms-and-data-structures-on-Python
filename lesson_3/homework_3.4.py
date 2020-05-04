# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint

nums = [randint(1, 10) for _ in range(10)]
counter = 0
max_num = 0

# Счиатем количесвто вхождений униакльных элементов в списке. Если текущий элемент встречался больше раз,
# чем предыдущий, то заменяем значения.
for num in set(nums):
    temp_counter = nums.count(num)
    if temp_counter > counter:
        max_num = num
        counter = temp_counter

print(f'В массиве {nums} чаще всего встречалось число {max_num}.')
