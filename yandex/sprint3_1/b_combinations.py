'''На клавиатуре старых мобильных телефонов каждой цифре
соответствовало несколько букв. Вам известно в каком порядке
были нажаты кнопки телефона, без учета повторов. Напечатайте
все комбинации букв, которые можно набрать такой последовательностью
sнажатий.'''

TEL: dict = {'2': 'abc',
             '3': 'def',
             '4': 'ghi',
             '5': 'jkl',
             '6': 'mno',
             '7': 'pqrs',
             '8': 'tuv',
             '9': 'wxyz'}


def bactrack(order, path, res):
    if order == '':
        res.append(path)
        return
    for letter in TEL[order[0]]:
        path += letter
        bactrack(order[1:], path, res)
        path = path[:-1]


def get_combinations(order):

    res = []
    bactrack(order, '', res)
    return res


if __name__ == '__main__':
    order = input()
    letters = get_combinations(order)
    for i in letters:
        print(i, end=' ')
