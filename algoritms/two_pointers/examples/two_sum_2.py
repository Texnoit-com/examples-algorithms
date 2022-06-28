'''Дан массив целых чисел arr и целое число X. Элементы в массиве не отсортированы.
Определите, существует ли в массиве два элемента, что сумма их равна X'''

def two_sum(arr: list, x: int) -> tuple:
    previous: set = set()
    for element in arr:
        difference = x- element
        if difference in previous:
            return element, difference
        else:
            previous.add(element)    
    return None, None

if __name__ == '__main__':
    array: int = [5, 7, 9, 12, 15, 18, 19, 20, 22]
    x: int = 27
    print(two_sum(array, x))
