'''Гоша реализовал структуру данных Дек, максимальный размер которого
определяется заданным числом. Методы push_back(x), push_front(x),
pop_back(), pop_front() работали корректно. .

Проверка решения
ID = 69382008
один тест н проходит по TL
'''

from dataclasses import dataclass
from typing import ClassVar, Union

COMMANDS: set = (
    'push_back',
    'push_front',
    'pop_front',
    'pop_back'
)


@dataclass
class Queue:
    n: int
    __queue: ClassVar = []

    def __str__(self):
        '''Вывод класса'''
        return ' '.join(map(str, self.__queue))

    def push_back(self, value) -> None:
        '''Добавление в конец очереди.'''
        if len(self.__queue) >= self.n:
            print('error')
            return
        self.__queue.append(value)

    def push_front(self, value) -> None:
        '''Добавление в начало очереди.'''
        if len(self.__queue) >= self.n:
            print('error')
            return
        self.__queue.insert(0, value)

    def pop_front(self) -> Union[int, str]:
        '''Извлечение с начало очереди.'''
        if len(self.__queue) <= 0:
            return 'error'
        return self.__queue.pop(0)

    def pop_back(self) -> Union[int, str]:
        '''Извлечение из конца очереди.'''
        if len(self.__queue) <= 0:
            return 'error'
        return self.__queue.pop()


def read_input():
    '''Метод ввода данных.'''
    n: int = int(input())
    m: int = int(input())
    q = Queue(m)
    for i in range(n):
        command = input().split()
        if command[0] not in COMMANDS:
            print('error command')
            return None
        if command[0] == 'push_back':
            q.push_back(int(command[1]))
        elif command[0] == 'push_front':
            q.push_front(int(command[1]))
        elif command[0] == 'pop_front':
            print(q.pop_front())
        elif command[0] == 'pop_back':
            print(q.pop_back())


if __name__ == '__main__':
    read_input()
