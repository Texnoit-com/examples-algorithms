'''Обход в ширину графа'''

from collections import defaultdict
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Graph:
    '''Класс ориентированного графа'''
    graph: ClassVar

    def __post_init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, start, finish):
        '''Добавления ребра к графу'''
        
        self.graph[start].append(finish)

    def BFS(self, vertex):
        '''Функция вывода обхода'''

        # Логический массив посещений
        visited = [False] * (max(self.graph) + 1)
        # очередь обхода BFS
        queue = []
        # добавление первого узла обхода
        queue.append(vertex)
        visited[vertex] = True

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=' ')
            # Проход по соседним вершинам
            for i in self.graph[vertex]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


if __name__ == '__main__':
    graph = Graph()
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)
    graph.addEdge(2, 3)
    graph.addEdge(3, 3)
    vertex: int = 2
    print(f"Обход в ширину для стартового узла {vertex}")
    graph.BFS(vertex)
