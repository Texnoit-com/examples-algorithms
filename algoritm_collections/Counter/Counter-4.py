'''уникальные значения, самые редкие элементы. Их можно найти срезом с шагом -1'''


from collections import Counter

age = [32, 33, 34, 33, 45, 34, 45, 23, 32, 23, 45, 23, 21, 25, 45]
age_counter = Counter(age)
age_unique = age_counter.most_common()[-1:]
print(age_unique)
