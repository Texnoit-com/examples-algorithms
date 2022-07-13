'''Обход в глубину графа'''

from collections import defaultdict
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class graphraph:
    '''Класс ориентированного графа'''
    graphraph: ClassVar

    def __post_init__(self):
        self.graphraph = defaultdict(list)

    def addEdgraphe(self, start, finish):
        '''Добавления ребра к графу'''
        self.graphraph[start].append(finish)

    def DFSUtil(self, v, visited):
        '''Функция вывода обхода'''

        visited.add(v)
        print(v, end=' ')

        for neigraphhbour in self.graphraph[v]:
            if neigraphhbour not in visited:
                self.DFSUtil(neigraphhbour, visited)

    def DFS(self, vertex):
        '''Функция рекурсии обхода'''

        visited = set()
        self.DFSUtil(vertex, visited)


if __name__ == '__main__':
    graph = graphraph()
    graph.addEdgraphe(0, 1)
    graph.addEdgraphe(0, 2)
    graph.addEdgraphe(1, 2)
    graph.addEdgraphe(2, 0)
    graph.addEdgraphe(2, 3)
    graph.addEdgraphe(3, 3)
    vertex: int = 2
    print(f"Обход в глубину для стартового узла {vertex}")
    graph.DFS(vertex)
