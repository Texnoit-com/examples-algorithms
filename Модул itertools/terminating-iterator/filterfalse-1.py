'''итератор печатает значения, которые возвращают false для переданной функции.'''

from itertools import filterfalse

print("Вывод значений, если функция возвращает false:")
print(list(filterfalse(lambda x: x % 2 == 0, [2, 4, 5, 7, 8])))
