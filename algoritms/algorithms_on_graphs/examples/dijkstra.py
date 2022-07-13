'''Поиск кратчайших путей от вершины источника. Алгоритм Дейкстры'''

import sys
from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Graph():
    vertices: int
    graph: ClassVar

    def __post_init__(self):
        self.graph = [[0 for column in range(self.vertices)]
                      for row in range(self.vertices)]

    def printSolution(self, dist):
        '''Вывод вершин'''
        print("Вершина \tРастояние до источника")
        for node in range(self.vertices):
            print(node+1, "\t", dist[node])

    def minDistance(self, dist, sptSet):
        '''Вычисление минимального расстояния'''
        min = sys.maxsize
        for u in range(self.vertices):
            if dist[u] < min and not(sptSet[u]):
                min = dist[u]
                min_index = u
        return min_index

    def dijkstra(self, src):
        '''Вычисление минимальны= маршрутов'''
        dist = [sys.maxsize] * self.vertices
        dist[src] = 0
        sptSet = [False] * self.vertices

        for cout in range(self.vertices):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True
            for y in range(self.vertices):
                if self.graph[x][y] > 0 and\
                   not(sptSet[y]) and \
                   dist[y] > dist[x] + self.graph[x][y]:

                    dist[y] = dist[x] + self.graph[x][y]
        self.printSolution(dist)


if __name__ == '__main__':
    graph = Graph(6)
    graph.graph = [[0, 3, 1, 3, 0, 0],
                   [3, 0, 4, 0, 0, 0],
                   [1, 4, 0, 0, 7, 5],
                   [3, 0, 0, 0, 0, 2],
                   [0, 0, 7, 0, 0, 4],
                   [0, 0, 5, 2, 4, 0]]

    graph.dijkstra(0)
