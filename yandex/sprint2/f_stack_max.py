from dataclasses import dataclass
from typing import ClassVar

COMMANDS = {
    'push': lambda q, value: q.push(int(value[0])),
    'pop': lambda q, value: q.pop(),
    'get_max': lambda q, value: q.get_max(),
}


@dataclass(repr=False, eq=False)
class Node:
    value: int
    next: ClassVar = None


@dataclass(repr=False, eq=False)
class StackMax:
    head: ClassVar = Node("head")
    size: ClassVar = 0

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.isEmpty():
            raise Exception('Стэк пустой')
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return 'error'
        self.head.next = self.head.next.next
        self.size -= 1

    def get_max(self):
        if self.isEmpty():
            return 'None'
        cur = self.head.next
        out = cur.value
        cur = cur.next
        while cur:
            if out < cur.value:
                out = cur.value
            cur = cur.next
        return out


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
