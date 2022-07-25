'''Двухсвязный список'''


from dataclasses import dataclass
from typing import ClassVar


@dataclass(repr=False, eq=False)
class Node:
    data: int
    previous: ClassVar = None
    next: ClassVar = None


@dataclass(repr=False, eq=False)
class DoublyLinkedList:
    head: ClassVar = None
    start_node: ClassVar = None
    last_node: ClassVar = None

    def append(self, data):
        '''Добавление элемента в список
        Если список пустой создает головной узел.'''
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            new_node = Node(data)
            self.last_node.next = new_node
            new_node.previous = self.last_node
            new_node.next = None
            self.last_node = new_node

    def left_display(self):
        '''Обход списка с лева на право.'''
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next

    def right_display(self):
        '''Обход списка с права на лево.'''
        current = self.last_node
        while current is not None:
            print(current.data, end=' ')
            current = current.previous


if __name__ == '__main__':
    L = DoublyLinkedList()
    L.append(1)
    L.append(2)
    L.append(3)
    L.append(4)
    L.left_display()
    print()
    L.right_display()
