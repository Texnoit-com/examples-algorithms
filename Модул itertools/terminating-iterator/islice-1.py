'''этот итератор выборочно выводит значения, указанные в его итерируемом контейнере,
переданном в качестве аргумента. Этот итератор принимает 4 аргумента: итерируемый контейнер,
начальную позицию, конечную позицию и шаг.'''


from itertools import islice

print("Выборочны значения списка:")
print(list(islice([2, 4, 5, 7, 8, 10, 20], 1, 6, 2)))
