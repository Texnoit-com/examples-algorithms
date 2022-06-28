'''Дан массив целых чисел arr и целое число X. Элементы в массиве отсортированы по возрастанию.
Определите, существует ли в массиве такой непрерывный подмассив, что сумма его элементов равна X'''


def subarray_sum(array: int, x: int) -> bool:
    right: int = 0
    current_sum: int = 0
    for left in range(len(array)):
        if left > 0:
            current_sum -= array[left - 1]
        while right < len(array) and current_sum < x:
            current_sum += array[right]
            right += 1
        if current_sum == x:
            return True

    return False


if __name__ == '__main__':
    array: int = [5, 7, 9, 12, 15, 18, 19, 20, 22]
    x: int = 57
    print(subarray_sum(array, x))
