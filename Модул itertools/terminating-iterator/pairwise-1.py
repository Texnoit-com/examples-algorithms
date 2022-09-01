'''pairwise() - возвращает итератор перекрывающих пары элементов последовательности'''


from itertools import pairwise

print("Выборочны значения списка:")
print(list(pairwise('ABCDEFG')))
