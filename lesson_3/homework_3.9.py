# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

m = int(input('Укажите количество строк, матрицы: '))
n = int(input('Укажите количество столбцов матрицы: '))
matrix = [[randint(1, 100) for x in range(n)] for y in range(m)]
max_of_min = 0
min_col = 0

# Сначала ищем минимальный элемент среди каждого столбца и потом сравниваем с максимальным значением столбца.
for col in range(n):
    min_col = matrix[0][col]
    for elem in range(m):
        if min_col > matrix[elem][col]:
            min_col = matrix[elem][col]
    if not max_of_min:
        max_of_min = min_col
    else:
        if min_col > max_of_min:
            max_of_min = min_col

for row in matrix:
    for item in row:
        print(f'{item:>5}', end='')
    print()

print(f'Элемент, который будет максимальным среди минимальных значений столбцов: {max_of_min}')
