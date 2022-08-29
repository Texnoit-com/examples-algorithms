'''Добавление элементов'''

from collections import OrderedDict

d = OrderedDict.fromkeys([])
d['Максим'] = 10
d['Владимир'] = 20
d['Иван'] = 30
print(d)

d.move_to_end('Максим')
print(d)

    d.popitem(last=True)
    print(d)
