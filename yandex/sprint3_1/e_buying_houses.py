'''Он нашёл n объявлений о продаже, где указана стоимость каждого
дома в алгосских франках. А у Тимофея есть k франков. Помогите ему
определить, какое наибольшее количество домов на Алгосах он сможет
приобрести за эти деньги.'''


def buying_houses(money, houses):
    houses = list(map(int, houses.split(' ')))
    money = list(map(int, money.split(' ')))
    houses.sort()
    price = 0
    count = 0
    for i in range(len(houses)):
        if houses[i] + price <= money[1]:
            price += houses[i]
            count += 1
    return count


if __name__ == '__main__':
    print(buying_houses(input(), input()))
    print(buying_houses('1000', '350 999 200'))
