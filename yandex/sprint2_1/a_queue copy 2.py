'''Гоша реализовал структуру данных Дек, максимальный размер которого
определяется заданным числом. Методы push_back(x), push_front(x),
pop_back(), pop_front() работали корректно. .

Проверка решения
ID = 69405428
'''

COMMANDS = {
    'push_back': lambda q, value: q.push_back(value[0]),
    'push_front': lambda q, value: q.push_front(value[0]),
    'pop_front': lambda q, value: q.pop_front(),
    'pop_back': lambda q, value: q.pop_back(),
}


class Dek:

    def __init__(self, amount):
        self.__dek = [None] * amount
        self.__max_n = amount
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def overflow(self):
        '''Переполнение'''
        if self.__size >= self.__max_n:
            return True

    def empty(self):
        '''dek пустой'''
        if self.__size <= 0:
            return True

    def push_back(self, value):
        '''Добавление в конец очереди.'''
        if self.overflow():
            return 'error'
        self.__dek[self.__tail] = value
        self.__tail = (self.__tail + 1) % self.__max_n
        self.__size += 1

    def push_front(self, value):
        '''Добавление в начало очереди.'''
        if self.overflow():
            return 'error'
        self.__dek[self.__head - 1] = value
        self.__head = (self.__head - 1) % self.__max_n
        self.__size += 1

    def pop_front(self):
        '''Извлечение с начало очереди.'''
        if self.empty():
            return 'error'
        value = self.__dek[self.__head]
        self.__dek[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_n
        self.__size -= 1
        return value

    def pop_back(self):
        '''Извлечение из конца очереди.'''
        if self.empty():
            return 'error'
        value = self.__dek[self.__tail - 1]
        self.__dek[self.__tail - 1] = None
        self.__tail = (self.__tail - 1) % self.__max_n
        self.__size -= 1
        return value


def read_input():
    '''Метод ввода данных.'''
    number_of_lines: int = int(input())
    amount: int = int(input())
    q = Dek(amount)
    for i in range(number_of_lines):
        command = input().split()
        result = COMMANDS[command[0]](q, command[1:])
        if result is not None:
            print(result)


if __name__ == '__main__':
    read_input()
