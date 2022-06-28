'''Дан массив целых чисел arr и целое число X. Элементы в массиве не отсортированы.
Определите, существует ли в массиве два элемента, что сумма их равна X'''

def two_sum(arr: list, x: int) -> tuple:
    arr.sort()
    left: int = 0
    right: int = len(arr)-1
    while left <= right:
        current_sum = arr[left]+arr[right]
        if current_sum == x:
            return arr[left], arr[right]
        if current_sum <x:
            left += 1
        else:
            right -= 1
    return None, None

if __name__ == '__main__':
    array: int = [5, 7, 9, 12, 15, 18, 19, 20, 22]
    x: int = 27
    print(two_sum(array, x))
