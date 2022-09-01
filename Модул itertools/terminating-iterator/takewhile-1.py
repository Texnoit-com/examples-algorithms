'''takewhile() - итератор является противоположностью dropwhile(), он
печатает значения до тех пор, пока функция не вернет false в первый раз'''

from itertools import takewhile

print("Выводит значения, пока функция не будет равна False:")
print(list(takewhile(lambda x : x % 2 == 0, [2, 4, 6, 7, 8, 10, 20])))
