#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2025/3/8 18:32
# @Author: ZhaoKe
# @File : segment_tree.py
# @Software: PyCharm
class SegmentTreeNode:
    def __init__(self, start, end, value=0):
        self.start = start
        self.end = end
        self.sum = value  # 区间和
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, nums):
        self.root = self.__build_tree(nums, 0, len(nums) - 1)

    def __build_tree(self, nums, start, end):
        if start > end:
            return None
        if start == end:
            return SegmentTreeNode(start, end, value=nums[start])
        mid = (start + end) // 2
        root = SegmentTreeNode(start, end)
        root.left = self.__build_tree(nums, start, mid)
        root.right = self.__build_tree(nums, mid + 1, end)
        root.sum = root.left.sum + root.right.sum
        return root

    def query_sum(self, root, start, end):
        if not root or start > root.end or end < root.start:
            return 0
        if start <= root.start and end >= root.end:
            return root.sum
        mid = (root.start + root.end) // 2
        return self.query_sum(root.left, start, min(mid, end)) + self.query_sum(root.right, max(mid + 1, start), end)

    def update(self, root, index, val):
        if not root:
            return
        if root.start == root.end == index:
            root.sum = val
            return
        mid = (root.start + root.end) // 2
        if index <= mid:
            self.update(root.left, index, val)
        else:
            self.update(root.right, index, val)
        root.sum = root.left.sum + root.right.sum


if __name__ == '__main__':
    nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
            31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
            73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
            127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
            179, 181, 191, 193, 197, 199, 211]
    seg_tree = SegmentTree(nums)
    print(seg_tree.query_sum(seg_tree.root, 1, 4))  # 输出: 26
    seg_tree.update(seg_tree.root, 2, 6)
    print(seg_tree.query_sum(seg_tree.root, 1, 4))  # 输出: 27
