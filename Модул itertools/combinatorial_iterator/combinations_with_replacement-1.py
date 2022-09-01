'''combinations_with_replacement - функция возвращает подпоследовательность
длины n из элементов итерируемого объекта, где n — аргумент, длина
последовательностей, сгенерированных функцией. Отдельные элементы могут
повторяться в функции комбинации с заменой.'''

from itertools import combinations_with_replacement

print("Комбинация списка")
print(list(combinations_with_replacement(['A', 2], 2)))
print()

print("Комбинация строк")
print(list(combinations_with_replacement("ABС", 2)))
print()

print("Комбинация списка через генератор")
print(list(combinations_with_replacement(range(4), 3)))
