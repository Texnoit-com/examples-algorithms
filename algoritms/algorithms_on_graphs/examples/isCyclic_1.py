'''Поиск циклов на графике ориентированных графов'''

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

    def isCyclicUtil(self, v, visited, recStack):
        '''Поиск цикла'''

        visited[v] = True
        recStack[v] = True
        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.isCyclicUtil(neighbour, visited, recStack):
                    return True
            elif recStack[neighbour]:
                return True
        recStack[v] = False
        return False

    def isCyclic(self):
        '''Проверка всех путей на цикличность'''

        visited = [False] * (self.vertices + 1)
        recStack = [False] * (self.vertices + 1)
        for node in range(self.vertices):
            if not visited[node]:
                if self.isCyclicUtil(node, visited, recStack):
                    return True
        return False


if __name__ == '__main__':
    graph = Graph(4)
    graph.addEdge(0, 1)
    graph.addEdge(0, 2)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)
    graph.addEdge(2, 3)
    graph.addEdge(3, 3)
    if graph.isCyclic():
        print('График имеет цикл')
    else:
        print('График не имеет циклов')
