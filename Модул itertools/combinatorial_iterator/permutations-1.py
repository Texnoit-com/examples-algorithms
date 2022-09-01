'''permutations - используется для генерации всех возможных перестаново
итерируемого объекта . Все элементы считаются уникальными на основе их 
положения, а не их значений. Эта функция принимает итерируемый объект и 
размер группы (group_size).'''


from itertools import permutations

print("Все перестановки списка:")
print(list(permutations([1, 'geeks'], 2)))
print()

print("Все перестановки строки:")
print(list(permutations('AB')))
print()

print("Все перестановки контейнера:")
print(list(permutations(range(3), 2)))
