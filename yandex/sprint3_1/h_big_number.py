'''Даны числа. Нужно определить, какое самое 
большое число можно из них составить.'''


def big_number(source_array):
    lenght = len(source_array)
    for i in range(lenght - 1):
        for j in range(0, lenght-i-1):
            var1 = source_array[j] + source_array[j+1]
            var2 = source_array[j + 1] + source_array[j]
            if var1 < var2:
                source_array[j], source_array[j+1] = source_array[j+1], source_array[j]
    print("".join(source_array))


if __name__ == '__main__':
    _ = input()
    source_array = input().split(' ')
    big_number(source_array)
