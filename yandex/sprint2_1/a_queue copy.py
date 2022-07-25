'''Гоша реализовал структуру данных Дек, максимальный размер которого
определяется заданным числом. Методы push_back(x), push_front(x),
pop_back(), pop_front() работали корректно. .

Проверка решения
ID = 69394324
один тест не проходит по TL - !!! все таки не проходит
Убрал специально все излишества с аннотацией и dataclasses
'''

COMMANDS = {
    'push_back': lambda q, value: q.push_back(value[0]),
    'push_front': lambda q, value: q.push_front(value[0]),
    'pop_front': lambda q, value: q.pop_front(),
    'pop_back': lambda q, value: q.pop_back(),
}


class Dek:

    def __init__(self, amount):
        self.amount = amount
    __dek = []

    def overflow(self):
        '''Переполнение'''
        if len(self.__dek) >= self.amount:
            return True

    def empty(self):
        '''dek пустой'''
        if len(self.__dek) <= 0:
            return True

    def push_back(self, value):
        '''Добавление в конец очереди.'''
        if self.overflow():
            return 'error'
        self.__dek.append(value)

    def push_front(self, value):
        '''Добавление в начало очереди.'''
        if self.overflow():
            return 'error'
        self.__dek.insert(0, value)

    def pop_front(self):
        '''Извлечение с начало очереди.'''
        if self.empty():
            return 'error'
        return self.__dek.pop(0)

    def pop_back(self):
        '''Извлечение из конца очереди.'''
        if self.empty():
            return 'error'
        return self.__dek.pop()


def read_input():
    '''Метод ввода данных.'''
    number_of_lines: int = int(input())
    amount: int = int(input())
    q = Dek(amount)
    for i in range(number_of_lines):
        
    for i in range(number_of_lines):
        command = input().split()
        result = COMMANDS[command[0]](q, command[1:])
        if result is not None:
            print(result)


if __name__ == '__main__':
    read_input()
