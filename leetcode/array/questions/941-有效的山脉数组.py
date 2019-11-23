# -*- coding: utf-8 -*- 
# @Time : 2019/11/23 上午11:04 
# @Author : yangchengkai
# @File : 941-有效的山脉数组.py
class Solution:
    def validMountainArray(self, A: [int]) -> bool:
        """
        O(N)，使用增减特性，用两个循环找到增减段并赋值为up，down,当循环结束后判断指针是否指向数组结尾，和updown字段。
        与官方解法一致
        :param A:
        :return:
        """
        if len(A) < 3:
            return False
        idx = 1
        up,down = False,False
        while idx < len(A):
            if A[idx-1] == A[idx]:
                return False
            elif A[idx-1] > A[idx]:
                break
            idx += 1
            up = True
        while idx < len(A):
            if A[idx-1] == A[idx]:
                return False
            elif A[idx] > A[idx-1]:
                break
            idx += 1
            down = True
        return idx == len(A) and up and down