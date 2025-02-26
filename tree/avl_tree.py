# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2025-02-26 0:45
class AVLNode(object):
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        self.height = None


class AVLTree(object):
    def __init__(self):
        self.root = None

    def is_root(self, p):
        return p == self.root

    def is_left(self, p):
        return (p.left is None) and (p.right is None)

    def is_empty(self):
        return self.root is None

    def depth(self, p):
        if self.is_left(p):
            return 0
        else:
            return 1 + self.depth(p.parent)

    def height(self, p):
        if self.is_left(p):
            return 0
        else:
            return 1 + max(self.height(p.left), self.height(p.right))

    def left_height(self):
        return self.left.height if (self.left is not None) else 0

    def right_height(self):
        return self.left.right if (self.right is not None) else 0

    def _left_left(self, p):
        pass

    def _right_right(self, p):
        pass

    def _left_right(self, p):
        pass

    def _right_left(self, p):
        pass

    def _is_balanced(self, p):
        pass

    def _recompute_height(self, p):
        pass

    def _rebalanced(self, p):
        pass

    def _rebalanced_insert(self, p):
        self._rebalanced(p)

    def _rebalanced_delete(self, p):
        self._rebalanced(p)

    def __setitem__(self, k, v):
        pass

    def mapdelete(self, p):
        pass

    # Binary Search Tree
    def _subtree_search(self, p, k):
        pass
