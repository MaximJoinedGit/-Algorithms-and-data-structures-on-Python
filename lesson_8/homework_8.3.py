# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
# по алгоритму поиска в глубину (Depth-First Search).
#
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

from random import randrange


def graph(edge):
    """
    Функция, генерирующая граф.
    :return: Список смежности.
    """
    graph_generate = []
    is_valid = False

    while not is_valid:
        req_nums = {i for i in range(edge)}
        graph_generate = [{randrange(0, edge) for _ in range(randrange(1, edge))} for _ in range(edge)]

        for i in range(edge):

            # Сначала мы убираем из сетов петли.
            if i in graph_generate[i]:
                graph_generate[i].remove(i)

            # Затем, проверяем все ли вершины связаны между собой.
            for j in graph_generate:
                if i in j:
                    req_nums.remove(i)
                    break

            if not graph_generate[i]:
                req_nums.add(i)

        # Если все верно, то в сете не должно остаться значений и можно поменять значение is_valid на True.
        if not req_nums:
            is_valid = True

    return graph_generate


def deep_first_search(any_graph, start, visited):
    """
    Рекурсивная функция обхода графа. Изменяет входной массив is_visited и показывает, была ли посещена точка
    в результате обхода функции.
    """
    visited[start] = True

    for x in range(len(any_graph[start])):
        for vertex in any_graph[start]:
            if not visited[vertex]:
                visited[vertex] = True
                deep_first_search(any_graph, vertex, visited)


if __name__ == '__main__':
    # Ввод.
    n = int(input('Введите количество вершин: '))
    p = int(input('Укажите начальную точку обхода графа: '))
    is_visited = [False] * n

    # Функции.
    new_graph = graph(n)
    deep_first_search(new_graph, p, is_visited)

    # Вывод.
    for x in range(n):
        print(f'{x} - {", ".join(map(str, new_graph[x]))}')
    for gr, vis in enumerate(is_visited):
        print(f'Вешина {gr} посещена? {"Да" if vis == True else "Нет"}')
