'''count - итератор равномерно распределенных значений.
Указывается стартовый элемент и шаг.'''


from itertools import count

cnt = count(start=0, step=2)

for i in range(10):
    print(next(cnt))
