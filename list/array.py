#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2025/3/4 13:16
# @Author: ZhaoKe
# @File : array.py
# @Software: PyCharm
def max_3(cur_nums) -> int:
    buf = [0, 0, 0]
    for i in range(1, len(cur_nums)):
        for j in range(3):
            if cur_nums[i] > buf[j]:
                # print("cur_nums[{}] > buf[{}]".format(i, j))
                for k in range(2, j, -1):
                    buf[k] = buf[k - 1]
                    # print("buf[{}] = buf[{}]".format(k, k-1))
                buf[j] = cur_nums[i]
                # print("buf[{}] = cur_nums[{}]".format(j, i))
                break
    return buf[2]


"""
1 1 2 3 4 5 6 7 8 9 1000
2 338 304 619 95 343 496 489 116 98 127
3 931 240 986 894 826 640 965 833 136 138
4 940 955 364 188 133 254 501 122 768 408
"""
if __name__ == '__main__':
    max_num = int(input())
    for ie in range(max_num):
        cur_nums = [int(it) for it in input().split(' ')]
        print(max_3(cur_nums))
