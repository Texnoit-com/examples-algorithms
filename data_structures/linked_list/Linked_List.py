'''Односвязный список'''

from dataclasses import dataclass
from typing import ClassVar


@dataclass(repr=False, eq=False)
class Node:
    data: int
    next: ClassVar = None


@dataclass(repr=False, eq=False)
class LinkedList:
    head: ClassVar = None
    last_node: ClassVar = None

    def append(self, data):
        '''Добавление элемента в список
        Если список пустой создает головной узел.'''
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        '''вывод элементов списка'''
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next


if __name__ == '__main__':
    L = LinkedList()
    L.append(1)
    L.append(2)
    L.append(3)
    L.append(4)
    L.display()
