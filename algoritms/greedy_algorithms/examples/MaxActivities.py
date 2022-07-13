'''Задано n действий с указанием времени их начала и окончания.
Выберите максимальное количество действий, которые может выполнять
один человек, предполагая, что человек может работать только над одним
действием одновременно.'''


from collections import OrderedDict


def printMaxActivities(actions: dict) -> None:

    acn = sorted(actions, key=actions.get(1))
    ord_actions = OrderedDict()
    for k in acn:
        ord_actions[k] = actions[k]

    i = acn[0]
    print(i, end=' ')
    for j in ord_actions:
        if ord_actions[j][0] >= ord_actions[i][1]:
            print(j, end=' ')
            i = j


if __name__ == '__main__':
    actions: dict = {
        'action2': [3, 4],
        'action3': [0, 6],
        'action5': [8, 9],
        'action6': [5, 9],
        'action1': [1, 2],
        'action4': [5, 7],
    }
    printMaxActivities(actions)
