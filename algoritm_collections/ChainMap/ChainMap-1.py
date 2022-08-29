'''Объединение словарей'''

from collections import ChainMap

letters = {'a': 1, 'b': 2}
vowels = {'a': 2, 'b': 0, 'c': 0, 'd': 0, 'e': 1}
chain = ChainMap(letters, vowels)

print(chain['b'])
