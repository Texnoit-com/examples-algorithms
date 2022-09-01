'''итератор выводит элементы после элемента, который дает значение в функции выборки.'''


from itertools import dropwhile

print("Вывод значений, если функция возвращает false:")
print(list(dropwhile(lambda x: x % 2 == 0, [2, 4, 5, 7, 8])))
