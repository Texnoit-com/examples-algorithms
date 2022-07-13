'''Поиск циклов на графике неорентированных графов'''

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
        '''Добавления двух ребер к графу'''
        self.graph[start].append(finish)
        self.graph[finish].append(start)

    def isCyclicUtil(self, v, visited, parent):
        '''Поиск цикла'''
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                if(self.isCyclicUtil(i, visited, v)):
                    return True
            elif parent != i:
                return True
        return False

    def isCyclic(self):
        '''Проверка всех путей на цикличность'''
        visited = [False]*(self.vertices)
        for i in range(self.vertices):
            if not visited[i]:
                if(self.isCyclicUtil
                   (i, visited, -1)):
                    return True
        return False


if __name__ == "__main__":
    graph = Graph(5)
    graph.addEdge(1, 0)
    graph.addEdge(1, 2)
    graph.addEdge(2, 0)
    graph.addEdge(0, 3)
    graph.addEdge(3, 4)
    if graph.isCyclic():
        print("График имеет цикл")
    else:
        print("График не имеет циклов")
