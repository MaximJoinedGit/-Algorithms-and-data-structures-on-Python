# 2. Закодируйте любую строку по алгоритму Хаффмана.

import heapq
from collections import Counter


# Класс, инициализирующий узел.
class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    # Функция обхода по элементам дерева. Если ветвь идёт влево, то добавляем к "коду" буквы "0", если вправо - "1".
    def walk(self, _code, acc):
        self.left.walk(_code, acc + "0")
        self.right.walk(_code, acc + "1")


# Класс, инициализирующий лист
class Leaf:
    def __init__(self, char):
        self.char = char

    # Присваиваем код для каждого листа. Если символ в строке всего один, то присваиваем "0".
    def walk(self, _code, acc):
        _code[self.char] = acc or "0"


def huffman(text: str) -> dict:
    """
    Функция кодирования Хаффмана.
    :param text: Текст, который нужно кодировать.
    :return: Словарь, где ключи - символы, а значения - коды, уникальные для каждого символа.
    """
    # Инициализируем список
    h = []

    # Заполняем список значениями: частота, счетчик, сам лист
    for char, freq in Counter(text).items():
        h.append((freq, len(h), Leaf(char)))

    # Делаем из списка кучу
    heapq.heapify(h)
    count = len(h)

    # Пока в куче есть по крайней мере 2 значения мы продолжаем цикл. Два значения с минимальной частотой мы объединяем
    # узел. Одно значение - вправо, другое - влево.
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    # Инициализируем словарь символов и заполним его кодом, уникальным для каждого символа, обойдя все элементы
    # с помощью фукции walk.
    _code = {}
    [(_freq, _count, root)] = h
    root.walk(_code, "")
    return _code


if __name__ == "__main__":
    s = input('Введите текст для кодировки: ')
    code = huffman(s)
    for ch in sorted(code):
        print(f"{ch}: {code[ch]}")
    print(" ".join(code[ch] for ch in s))
