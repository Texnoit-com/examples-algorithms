'''Метод most_common(n) ищет n самых повторяющихся элементов'''


from collections import Counter

age = [32, 33, 34, 33, 45, 34, 45, 23, 32, 23, 45, 23, 21, 25, 45]
age_counter = Counter(age)
age_n3 = age_counter.most_common(2)
print(age_n3)
