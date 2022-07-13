'''Мама Васи хочет знать, что сын планирует делать и когда. 
Помогите ей: напишите функцию solution, определяющую индекс 
первого вхождения передаваемого ей на вход значения в связном 
списке, если значение присутствует.'''


class Node:
    def __init__(self, value, next_item=None):
        self.value = value  
        self.next_item = next_item
def solution(node, elem):
    count = 0
    while elem != count:
        if node == None:
            return -1
        if elem == node.value:
            return count
        else:
            node = node.next_item
            count += 1
def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node26")
    # result is idx == 2
if __name__ == '__main__':
    test()
