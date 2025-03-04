#!/user/zhao/miniconda3/envs/torch-0
# -*- coding: utf_8 -*-
# @Time : 2025/3/4 9:26
# @Author: ZhaoKe
# @File : numberq.py
# @Software: PyCharm

def dec2bin(number: int):
    res = ""
    if number == 0:
        return "0"
    while number > 0:
        if (number & 1) == 1:
            res = "1" + res
        else:
            res = "0" + res
        number >>= 1
    return str(res)


def dec2oct(number: int):
    res = ""
    if number == 0:
        return "0"
    mapper = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    while number > 0:
        fac, rem = divmod(number, 16)
        # print("fac:{}, rem:{}".format(fac, rem))
        if rem < 10:
            res = str(rem) + res
        else:
            res = mapper[rem] + res
        number = fac
    return str(res)


def PopCount(n):
    cnt = 0
    while n > 0:
        if n & 1:
            cnt += 1
        n >>= 1
    return cnt


if __name__ == '__main__':
    n = int(input())
    print(PopCount(n))

    # max_num = int(input())
    # ind = 0
    # for i in range(max_num):
    #     cur_num = int(input())
    #     print("case #{}:".format(ind))
    #     print("{} {}".format(dec2bin(cur_num), dec2oct(cur_num)))
    #     ind += 1
