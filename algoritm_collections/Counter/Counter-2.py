'''Метод elements() преобразует результаты подсчета в итератор'''


from collections import Counter

age_counter = Counter({45: 4, 23: 3, 32: 2, 33: 2, 34: 2, 21: 1, 25: 1})
age = list(age_counter.elements())
print(age)
