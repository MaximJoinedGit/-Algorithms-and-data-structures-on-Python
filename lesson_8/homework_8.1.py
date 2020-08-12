# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.


def handshakes_first(n):
    """
    Функция создает матрицу смежности, считая все рукопожатия. Так как она считает рукопожатие первого человека второму
    и второго первому результатом будет сумма рукопожатий, деленная на два. На вход в граф сразу же исключается
    рукопожатие самому себе.
    """
    graph = [[1 if not handshake == friend else 0 for handshake in range(n)] for friend in range(n)]
    total = 0
    for num in range(len(graph)):
        total += sum(graph[num])
    return total // 2


def handshakes_second(n):
    """
    Функция создает списки смежности. Результатом будет длина списка, куда войдут только те значения, которые не равны
    друг другу и встречаются только один раз.
    """
    graph = list()
    for first_friend in range(n):
        for second_friend in range(n):
            if first_friend < second_friend:
                graph.append((first_friend, second_friend))
    return len(graph)


if __name__ == '__main__':
    for x in range(2, 100):
        assert handshakes_first(x) == handshakes_second(x)
    friends = int(input('Введите количество друзей: '))
    print(f'Итого рукопожатий среди {friends} друзей - {handshakes_first(friends)}')
    print(f'Итого рукопожатий среди {friends} друзей - {handshakes_second(friends)}')
