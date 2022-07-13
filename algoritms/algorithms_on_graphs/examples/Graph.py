'''Пример класса для создания списков смежности графов'''

from dataclasses import dataclass
from typing import ClassVar


@dataclass
class AdjNode:
    vertex: int
    next: ClassVar = None


@dataclass
class Graph:
    vertices: int
    graph: ClassVar = []

    def __post_init__(self):
        self.graph = [None] * vertices

    def add_edge(self, src, dest):
        '''Добавление ребра в неориентированный граф'''
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node
        # Добавление исходного узла к целевому
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        '''Вывод графа'''
        for i in range(self.vertices):
            print(f'Список смежности вершины {i}\n', end='')
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


if __name__ == '__main__':
    vertices = 5
    graph = Graph(vertices)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
