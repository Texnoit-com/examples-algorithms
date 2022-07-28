'''У вас есть информация о росте Васиных накоплений — сколько у Васи в копилке 
было денег в каждый из дней. Ваша задача — по заданной стоимости велосипеда 
определить первый день, в которой Вася смог бы купить один велосипед, и первый
день, в который Вася смог бы купить два велосипеда.
Подсказка: решение должно работать за O(log n).'''


def binarySearch(money, price, left, right):
    if (right <= left and left != 0):
        return -1
    middle = (left + right) // 2
    if (money[middle] >= price and (money[middle - 1] < price or middle == 0)):
        return middle + 1
    elif price <= money[middle]:
        return binarySearch(money, price, left, middle)
    else:
        return binarySearch(money, price, middle + 1, right)


def two_bicycles(accumulation, price):
    accumulation = list(map(int, accumulation.split(' ')))
    lenght = len(accumulation)
    day_one_bicycles = binarySearch(accumulation, price, 0, lenght)
    day_two_bicycles = binarySearch(accumulation, price*2, 0, lenght)
    print(day_one_bicycles, end=' ')
    print(day_two_bicycles)


if __name__ == '__main__':
    _ = input()
    accumulation = input()
    price = int(input())
    two_bicycles(accumulation, price)
