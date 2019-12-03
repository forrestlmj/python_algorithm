# -*- coding: utf-8 -*- 
# @Time : 2019/11/30 下午10:47 
# @Author : yangchengkai
# @File : 121买卖股票的最佳时机.py

import queue
import sys
class Solution:
    def maxProfit(self, prices) -> int:
        """
        时间复杂度必为O(N)
        空间复杂度用栈为O(N),但是用最小值保持即可。
        :param prices:
        :return:
        """
        s = queue.deque()
        if not prices:
            return 0
        s.append(prices[0])
        profit = -sys.maxsize
        for i in prices[1:]:
            if s:
                profit = max(profit,i-s[-1])
                if i < s[-1]:
                    s.append(i)
        return max(0,profit)