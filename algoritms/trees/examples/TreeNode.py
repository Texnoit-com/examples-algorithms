'''Реализация двоичного дерева и методов обхода PRE IN  POST'''

from dataclasses import dataclass
from typing import ClassVar


@dataclass
class TreeNode:
    value: int
    left: ClassVar = None
    right: ClassVar = None

    def pre_order(self, node) -> None:
        if node:
            print(node.value)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node) -> None:
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value)

    def in_order(self, node) -> None:
        if node:
            self.in_order(node.left)
            print(node.value)
            self.in_order(node.right)


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)

    tree.post_order(tree)
