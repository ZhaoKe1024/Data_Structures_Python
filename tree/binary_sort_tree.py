# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2025-02-26 0:39
from collections import deque


class TriNode(object):
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def is_leaf(self):
        return (self.left is None) and (self.right is None)

    def toString(self):
        return str(self.data)


class BinarySortTree(object):
    def __init__(self, values=None):
        self.root = None
        if values is not None:
            if len(values) > 0:
                for i in range(len(values)):
                    self.add(values[i])

    def is_empty(self) -> bool:
        return self.root is None

    def search_node(self, key) -> TriNode:
        # O(log_2{n} ~ O(n))
        p = self.root
        while (p is not None) and (key != p.data):
            if key < p.data:
                p = p.left
            else:
                p = p.right
        return p if (p is not None) else None

    def add(self, x) -> bool:
        # O(log_2{n} ~ O(n))
        if self.root is None:
            self.root = TriNode(data=x)
        else:
            p = self.root
            parent = None
            while p is not None:
                if x == p.data:
                    return False
                parent = p
                if x < p.data:
                    p = p.left
                else:
                    p = p.right
            if x < parent.data:
                parent.left = TriNode(data=x, parent=parent, left=None, right=None)
            else:
                parent.right = TriNode(data=x, parent=parent, left=None, right=None)
        return True

    def remove(self, key) -> TriNode:
        p = self.search_node(key)
        if (p is not None) and (p.left is not None) and (p.right is not None):
            insucc = self.__first(p.right)
            temp = p.data
            p.data = insucc.data
            insucc.data = temp
            p = insucc
        if (p is not None) and (p is self.root):
            if self.root.left is not None:
                self.root = p.left
            else:
                self.root = p.right
            if self.root is not None:
                self.root.parent = None
            return p.data
        if (p is not None) and (p is p.parent.left):
            if p.left is not None:
                p.parent.left = p.left
                p.left.parent = p.parent
            else:
                p.parent.left = p.right
                if p.right is not None:
                    p.right.parent = p.parent
        if (p is not None) and (p is p.parent.right):
            if p.left is not None:
                p.parent.right = p.left
                p.left.parent = p.parent
            else:
                p.parent.right = p.right
                if p.right is not None:
                    p.right.parent = p.parent
        return p.data if (p is not None) else None

    @staticmethod
    def __first(p: TriNode) -> TriNode:
        if p is not None:
            while p.left is not None:
                p = p.left
        return p

    def __next(self, p: TriNode):
        if p is not None:
            if p.right is not None:
                return self.__first(p.right)
            while p.parent is not None:
                if p.parent.left is p:
                    return p.parent
                p = p.parent
        return None

    def toString(self) -> str:
        res = "["
        p = self.__first(self.root)
        while p is not None:
            res += p.toString() + " "
            p = self.__next(p)
        return res + "]"

    def size(self):
        pass

    def clear(self):
        self.root = None

    def contains(self, item):
        pass

    def addAll(self, values):
        for i in range(len(values)):
            self.add(values[i])

    def previous(self, p: TriNode) -> TriNode:
        pass

    def last(self: TriNode) -> TriNode:
        pass


def level_traversal(tree):
    dq = deque()
    # dq = tree


if __name__ == '__main__':
    values = [54, 18, 81, 12, 36, 6, 40, 57, 76, 99, 66]
    bst = BinarySortTree(values=values)
    print(bst.toString())
    print()
