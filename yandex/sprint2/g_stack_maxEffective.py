from dataclasses import dataclass
from typing import ClassVar

COMMANDS = {
    'push': lambda q, value: q.push(int(value[0])),
    'pop': lambda q, value: q.pop(),
    'get_max': lambda q, value: q.get_max(),
    'str':  lambda q, value: q.__str__(),
}


@dataclass(repr=False, eq=False)
class Node:
    value: int
    max_node: int
    next: ClassVar = None


@dataclass(repr=False, eq=False)
class StackMax:
    head: ClassVar = Node("head", None)
    size: ClassVar = 0
    max_stack: ClassVar = None

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]

    def isEmpty(self):
        return self.size == 0

    def push(self, value):
        if self.max_stack is None or self.max_stack < value:
            self.max_stack = value
        node = Node(value, self.max_stack)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return 'error'
        self.head.next = self.head.next.next
        self.max_stack = self.head.max_node
        print(self.head.max_node)
        self.size -= 1

    def get_max(self):
        return self.max_stack


def read_input():
    '''Метод ввода данных.'''
    number_of_lines: int = int(input())
    q = StackMax()
    for i in range(number_of_lines):
        command = input().split()
        result = COMMANDS[command[0]](q, command[1:])
        if result is not None:
            print(result)


if __name__ == '__main__':
    read_input()
