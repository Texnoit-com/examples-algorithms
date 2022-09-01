'''groupby() - Создаёт итератор по сгруппированным элементам переданного объекта'''

from itertools import groupby


def grouper(item):
    """Будем использовать эту функцию для группировки сортировки."""
    return item['country']


data = [
    {'city': 'Москва', 'country': 'Россия'},
    {'city': 'Новосибирск', 'country': 'Россия'},
    {'city': 'Пекин', 'country': 'Китай'},
]

for key, group_items in groupby(data, key=grouper):
    print('Key: %s' % key)
    for item in group_items:
        print('Item: %s' % item)
