# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.
# Сортировка в решении не используется.

from random import randint


def generator(length):
    """
    Функция-генератор. Принимает на вход натуральное число m и генерирует список уникальных чисел длиной 2m + 1.
    """
    lst = list()
    while len(lst) < length * 2 + 1:
        num = randint(-100, 100)
        if num not in lst:
            lst.append(num)
    return lst


def middle(array):
    """
    Функция по определению медианы списка. Проходит циклом по каждому элементу, останавливается и возвращает число, при
    котором количество бОльших и мЕньших ему элементов будут равны.
    """
    for num in array:
        mid = 0
        for j in range(len(array)):
            if array[j] > num:
                mid += 1
            elif array[j] < num:
                mid -= 1
        if mid == 0:
            return num


if __name__ == '__main__':
    m = 10
    for i in range(1000):
        arr = generator(m)
        assert middle(arr) == sorted(arr)[10]
    arr = generator(m)
    print(f'Число {middle(arr)} является медианой списка {arr}')
