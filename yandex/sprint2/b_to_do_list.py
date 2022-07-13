'''Васе нужно распечатать свой список дел на сегодня. Помогите ему:
напишите функцию, которая печатает все его дела'''


def solution(node):
    while node != None:
        print(node.value)
        node = node.next_item
