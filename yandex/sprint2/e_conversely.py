'''Вася решил запутать маму —– делать дела в обратном порядке.
Список его дел теперь хранится в двусвязном списке. Напишите
функцию, которая вернёт список в обратном порядке.'''


class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(node):
    n = node
    m = n.next
    n.next = None
    n.prev = m
    while m is not None:
        m.prev = m.next
        m.next = n
        n = m
        m = m.prev
    node = n
    return node


def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")
    node0.next = node1
    node1.prev = node0
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2


if __name__ == '__main__':
    test()
