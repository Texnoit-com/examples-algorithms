'''tee() - cоздаёт несколько итераторов для одного итерируемого объекта​.'''

from itertools import tee

iter1, iter2, iter3 = tee([1, 2, 3], 3)

print(list(iter1))
print(list(iter2))
print(list(iter3))
