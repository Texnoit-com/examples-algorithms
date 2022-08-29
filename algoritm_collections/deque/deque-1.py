'''Двусторонняя очередь'''

from collections import deque

seq = [1, 2, 3, 4, 5]
deq = deque(seq)
deq.append(6)      # добавление в конец
deq.appendleft(0)  # добавление в начало
print(deq)

deq.extend([7, 8, 9])      # добавление в конец
deq.extendleft([-1, -2, -3])  # добавление в начало
print(deq)
