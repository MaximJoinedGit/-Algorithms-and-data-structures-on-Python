# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин,
# которые необходимо обойти.

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    """
    Функция на основе алгоритма Дейкстры, которая возвращает:
    - список кратчайших путей и их вес до всех остальных вершин
    - словарь вершин, через которые пройдет кратчайший путь
    """
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    way = {vertex: 'Нет пути' for vertex in range(length)}

    cost[start] = 0
    way[start] = 'Начальная вершина'
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    for rev in range(length):
        if not parent[rev] == -1:
            way[rev] = [rev]
            while way[rev][-1] >= 0:
                way[rev].append(parent[way[rev][-1]])
        if way[rev][-1] == -1:
            way[rev].remove(-1)

    return cost, way


if __name__ == '__main__':
    s = int(input('От какой вершины идти: '))
    cost_from, ways_from = dijkstra(g, s)

    print(f'Начальная вершина: {s}')
    for v, w in ways_from.items():
        if not w == 'Начальная вершина' and not w == 'Нет пути':
            print(f'Путь в вершину {v} из начальной: {" -> ".join(map(str, w[::-1]))}. Вес пути {cost_from[v]}')
        elif w == 'Нет пути':
            print(f'Нет пути до вершины {v}')
