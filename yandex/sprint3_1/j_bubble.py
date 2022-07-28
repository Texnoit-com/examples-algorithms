'''Алгоритм пузырковой сортировки'''


def bubble_sort(source_array):
    flag = 1
    lenght = len(source_array)
    for i in range(lenght):
        for j in range(0, lenght-i-1):
            if source_array[j] > source_array[j+1]:
                source_array[j], source_array[j+1] = source_array[j+1], source_array[j]
                flag = 1
        if flag == 1:
            for element in source_array:
                print(element, end=' ')
            print()
            flag = 0


if __name__ == '__main__':
    _ = input()
    source_array = list(map(int, input().split(' ')))
    bubble_sort(source_array)
