'''combinations- этот итератор печатает все возможные комбинации (без замены)
контейнера, переданного в аргументах, в указанном размере группы без повторений.'''


from itertools import combinations

print("Комбинация списка:")
print(list(combinations(['A', 2], 2)))
print()

print("Комбинация строк:")
print(list(combinations('ABC', 2)))
print()

print("Комбинация списка через генератор:")
print(list(combinations(range(4), 3)))
