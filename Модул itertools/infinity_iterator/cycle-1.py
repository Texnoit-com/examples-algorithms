'''cycle - итератор циклически возвращает элементы итерируемого объекта'''


from itertools import cycle

cyls = cycle([1, 2, 3])
print(next(cyls))  # 1
print(next(cyls))  # 2
print(next(cyls)) # 3
print(next(cyls))  # 1
