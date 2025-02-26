# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2025-02-26 0:00
from collections import deque
from typing import List


class BinaryNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return self.data

    def is_leaf(self) -> bool:
        return (self.left is None) and (self.right is None)


class BinaryTree(object):
    def __init__(self, prelist):
        self.i = 0
        self.root = self.__create(prelist)
        # else:
        #     pass

    def __create(self, prelist):
        p = None
        if self.i < len(prelist):
            elem = prelist[self.i]
            self.i += 1
            if elem is not None:
                p = BinaryNode(data=elem)
                p.left = self.__create(prelist)
                p.right = self.__create(prelist)
        return p

    def is_empty(self):
        return self.root is None

    def level(self, key)->int:
        pass

    def size(self):
        return self.__size(self.root)

    def search(self, key) -> BinaryNode:
        pass

    def __size(self, p):
        if p is None:
            return 0
        else:
            return 1 + self.__size(p.left) + self.__size(p.right)

    def insert(self):
        pass

    def __str__(self):
        return

    def __to_string(self, p: BinaryNode):
        if p is None:
            return "^"
        else:
            return p.data.__str__() + " " + self.__to_string(p.left) + self.__to_string(p.right)

    # Binary tree pre order, middle order, and post traversal implemented through recursion and stack respectively
    def pre_order(self, mode="recursion"):
        if mode == "recursion":
            print("pre-order traversal(recursion)")
            self.__pre_order(self.root)
            print()
        elif mode == "stack":
            print("pre-order traversal(stack)")
            self.__pre_order_stack()
        else:
            raise ValueError("Unknown mode, please choose between [\"recursion\", \"stack\"].")

    def __pre_order(self, p: BinaryNode):
        if p is not None:
            print(p.data, end=' ')
            self.__pre_order(p.left)
            self.__pre_order(p.right)

    def __pre_order_stack(self):
        stack = deque()
        p = self.root
        while (p is not None) or (len(stack)>0):
            if p is not None:
                print(p.data+" ", end='')
                stack.append(p)
                p = p.left
            else:
                print("^ ", end='')
                p = stack.pop()
                p = p.right
        print()

    def in_order(self):
        pass

    def post_order(self):
        pass


if __name__ == '__main__':
    prelist = ['A', 'B', 'D', None, 'H', None, None, 'E', 'I', None, None, 'J', None, None, 'C', 'F', None, 'K', None, None, 'G', None, None]
    bitree = BinaryTree(prelist=prelist)
    bitree.pre_order(mode="recursion")
    bitree.pre_order(mode="stack")
