'''Рита захотела отсортировать свой новый гардероб по цветам.
Сначала должны идти вещи розового цвета, потом —– жёлтого, и в
конце —– малинового. Помогите Рите справиться с этой задачей.
Розовый цвет обозначен 0, жёлтый —– 1, малиновый –— 2.'''


def wardrobe(clothes):
    clothes = clothes.split()
    less = []
    equal = []
    greater = []
    for i in clothes:
        if i == '0':
            less.append(i)
        elif i == '1':
            equal.append(i)
        else:
            greater.append(i)
    return less + equal + greater


if __name__ == '__main__':
    _ = input()
    print(*wardrobe(input()))
