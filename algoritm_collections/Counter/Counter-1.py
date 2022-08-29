'''Подсчет возрастных групп'''


from collections import Counter

age = [32, 33, 34, 33, 45, 34, 45, 23, 32, 23, 45, 23, 21, 25, 45]
age_counter = Counter(age)
print(age_counter)
