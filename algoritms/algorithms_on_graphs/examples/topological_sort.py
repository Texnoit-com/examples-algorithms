'''Топологическая сортировка вершин'''

from collections import defaultdict
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Graph():
    '''Класс ориентированного графа'''
    vertices: int
    graph: ClassVar

    def __post_init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, start, finish):
        '''Добавления ребра к графу'''
        self.graph[start].append(finish)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        stack.append(v)

    def topologicalSort(self):
        '''Сортировка вершин'''
        visited = [False]*self.vertices
        stack = []

        for i in range(self.vertices):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        print(stack[::-1])


if __name__ == '__main__':
    graph = Graph(6)
    graph.addEdge(5, 2)
    graph.addEdge(5, 0)
    graph.addEdge(4, 0)
    graph.addEdge(4, 1)
    graph.addEdge(2, 3)
    graph.addEdge(3, 1)

    graph.topologicalSort()
