# -*- coding: utf-8 -*-
# @Author : ZhaoKe
# @Time : 2025-02-26 0:45
class AVLNode(object):
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        self.bf = 0


class AVLTree(object):
    def __init__(self):
        self.root = None

    def is_root(self, p):
        return p == self.roo

    def is_leaf(self, p):
        return (p.left is None) and (p.right is None)

    def is_empty(self):
        return self.root is None

    def depth(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + self.depth(p.parent)

    @staticmethod
    def _height(node):
        return -1 if not node.height else node.height

    def insert(self, data):
        if not self.root:
            self.root = AVLNode(data=data)
        else:
            p = self.root
            while True:
                if data == p.data:
                    print("{} exists.".format(data))
                    break
                elif data < p.data:
                    if not p.left:
                        cur_node = AVLNode(data, p)
                        p.left = cur_node
                        self.__insert_rebalance(cur_node)
                        break
                    else:
                        p = p.left
                else:
                    if not p.right:
                        cur_node = AVLNode(data, p)
                        p.right = cur_node
                        self.__insert_rebalance(cur_node)
                        break
                    else:
                        p = p.right

        return True

    def __insert_rebalance(self, node):
        par = node.parent
        while par:
            if node is par.left:
                par.bf -= 1
            else:
                par.bf += 1
            if par.bf == 0:
                return
            if par.bf == -2:
                if node.bf == 1:
                    self.__rotate_left_right(par, node)
                    break
                else:
                    self.__rotate_right(par, node)
                    break
            elif par.bf == 2:
                if node.bf == -1:
                    self.__rotate_right_left(par, node)
                    break
                else:
                    self.__rotate_left(par, node)
                    break
            node = par
            par = par.parent

    def __rotate_left(self, parent, node):
        new_node = node.left
        node.left = parent
        parent.right = new_node
        if new_node:
            new_node.parent = parent
        if parent is self.root:
            self.root = node
        else:
            if parent is parent.parent.left:
                parent.parent.left = node
            else:
                parent.parent.right = node
        node.parent = parent.parent
        parent.parent = node
        node.bf = parent.bf = 0

    def __rotate_right(self, parent, node):
        """
                2(8)      |        0(6)
               /   \      |     /       \
           -1(6)   (13)0  |   1(2)      (8)0
            /  \          |       \      /    \
        1(2)    (7)0       |     0(3)  0(7)   (13)0
          \                |
          0(3)_inserted   |
        :param parent:
        :param node:
        :return:
        """
        new_node = node.right
        node.right = parent
        parent.left = new_node
        if new_node:
            new_node.parent = parent
        if parent is self.root:
            self.root = node
        else:
            if parent is parent.parent.left:
                parent.parent.left = node
            else:
                parent.parent.right = node
        node.parent = parent.parent
        parent.parent = node
        node.bf = parent.bf = 0

    def __rotate_left_right(self, parent, node):
        node_right = node.right
        bf = node_right.bf
        self.__rotate_left(node, node_right)
        self.__rotate_right(parent, node_right)
        if bf == 0:
            node.bf = node_right.bf = parent.bf = 0
        elif bf == -1:
            parent.bf = 1
            node.bf = node_right.bf = 0
        else:
            node.bf = -1
            node_right.bf = parent.bf = 0

    def __rotate_right_left(self, parent, node):
        node_left = node.left
        bf = node_left.bf
        self.__rotate_left(node, node_left)
        self.__rotate_right(parent, node_left)
        if bf == 0:
            node.bf = node_left.bf = parent.bf = 0
        elif bf == -1:
            node.bf = 1
            parent.bf = node_left.bf = 0
        else:
            parent.bbf = -1
            node_left.bf = node.bf = 0

    def delete_key(self, key):
        # reference: https://www.cnblogs.com/yscl/p/10077607.html
        cur = self.find(key)
        if cur:
            if cur.left and cur.right:
                self.__delete3()
            elif not cur.left and not cur.right:
                self.__delete1()
            else:
                self.__delete2()
        else:
            print("{} not exist.".format(key))

    def __delete1(self):
        pass

    def __delete2(self):
        pass

    def __delete3(self):
        pass

    def _recompute_height(self, p):
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

    def find(self, key):
        p = self.root
        while p:
            if p.data == key:
                return p
            if key < p.data:
                p = p.left
            else:
                p = p.right
        return None

    # def find(self, key):
    #     return self.__find(self.root, key=key)
    #
    # def __find(self, node, key):
    #     if not node:
    #         return None
    #     elif key == node.data:
    #         return node
    #     elif key < node.data:
    #         return self.__find(node=node.left, key=key)
    #     else:
    #         return self.__find(node=node.right, key=key)
