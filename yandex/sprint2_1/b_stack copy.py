'''Калькулятор

Проверка решения
ID = 69394480
'''
from dataclasses import dataclass
from typing import ClassVar, Optional

OPERATIONS: dict = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b
}


@dataclass(repr=False, eq=False)
class Stack:
    __items: ClassVar

    def __post_init__(self):
        '''Первоначальное присваивание'''
        self.__items = []

    def push(self, value: int) -> None:
        '''Поместить элемент'''
        return self.__items.append(value)

    def pop(self) -> Optional[int]:
        '''Извлечь элемент'''
        try:
            return self.__items.pop()
        except IndexError:
            pass

    def __str__(self):
        '''Вывод класса'''
        return ' '.join(map(str, self.__items))


def read_input() -> int:
    '''Метод ввода данных.'''
    values = input().split()
    stack = Stack()
    for value in values:
        if value not in OPERATIONS:
            stack.push(int(value))
        else:
            operator_2 = stack.pop()
            operator_1 = stack.pop()
            result = OPERATIONS[value](operator_1, operator_2)
            stack.push(result)
    return stack.pop()


if __name__ == '__main__':
    print(read_input())
