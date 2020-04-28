# 1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

first = 5
second = 6

print(f'Первое число: {first} ({bin(first)})\n'
      f'Второе число: {second} ({bin(second)})')
print(f'Первое И второе: {first & second} ({bin(first & second)})\n'
      f'Первое ИЛИ второе: {first | second} ({bin(first | second)})\n'
      f'Исключающее ИЛИ: {first ^ second} ({bin(first ^ second)})')
print(f'Не первое: {~first} ({bin(~first)})\n'
      f'Не второе: {~second} ({bin(~second)})')
print(f'Побитовый сдвиг влево: {first << 2} ({bin(first << 2)})\n'
      f'Побитовый сдвиг вправо: {first >> 2} ({bin(first >> 2)})')
