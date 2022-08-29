def broken_search(nums, target) -> int:
    '''Поиск элемента в 'сломанном' кольцевом
    отсортированном массиве'''

    left, right = 0, len(nums) - 1

    while left <= right:
        median = (left + right) // 2
        if nums[median] == target:
            return median
        if nums[left] <= nums[median]:
            '''Проверка вхождения искомого элемента в интервал
            левой части массива, если элемент входит сдвигаем
            правую границу влево,
            иначе сдвигаем левую границу вправо'''
            if nums[left] <= target < nums[median]:
                right = median - 1
            else:
                left = median + 1
        else:
            '''Проверка вхождения искомого элемента в интервал
            правой части массива'''
            if nums[median] < target <= nums[right]:
                left = median + 1
            else:
                right = median - 1
    return -1


if __name__ == '__main__':
    def test():
        arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
        assert broken_search(arr, 5) == 6

    test()
