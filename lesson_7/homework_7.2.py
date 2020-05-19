# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import uniform


def merge_sort(array: list):
    """
    Рекурсивная функция. Будет делить массив на левую и правую часть и вызывать саму себя,
    пока длина массива в параметрах функции не будет меньше двух.
    """
    if len(array) < 2:
        return array
    left = merge_sort(array[:len(array) // 2])
    right = merge_sort(array[len(array) // 2:])
    new_array = list()

    # Сравнивая элементы в списках, пока они не кончатся, мы формируем новый сортированный массив.
    while left and right:
        new_array.append(right.pop(0)) if left[0] > right[0] else new_array.append(left.pop(0))
    while left:
        new_array.append(left.pop(0))
    while right:
        new_array.append(right.pop(0))

    return new_array


if __name__ == '__main__':
    n = 10
    for i in range(1000):
        arr = [uniform(0, 49).__round__(3) for _ in range(n)]
        assert merge_sort(arr) == sorted(arr)
    arr = [uniform(0, 49).__round__(3) for _ in range(n)]
    print(f'Исходный массив: {arr}.')
    print(f'Отсортированный массив: {merge_sort(arr)}')
