'''compress() - этот итератор выборочно выбирает значения из переданного контейнера 
в соответствии со значением логического списка, переданным вторым аргументом. 
Аргументы, соответствующие логическому значению true, печатаются, иначе все они пропускаются.'''

from itertools import compress

print("Вывод элементов, в индексе маски которого стоит значение True или 1:")
print(list(compress('GEEKSFORGEEKS', [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0])))
