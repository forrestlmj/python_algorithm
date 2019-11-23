# -*- coding: utf-8 -*- 
# @Time : 2019/11/23 上午11:23 
# @Author : yangchengkai
# @File : 532-数组中的K-diff数对.py
"""
超时解法
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        re = set()
        idx = 0
        while idx < len(nums):
            a = nums[idx]
            if a+k in nums[idx+1:]:
                re.add((a,a+k))
            idx += 1
        return len(re)

"""
class Solution:
    def findPairs(self, nums: [int], k: int) -> int:
        """
        O(N)主要卡在细节上，思想上用set进行去重没错，主要是set的值存储最小即可。

        :param nums:
        :param k:
        :return:
        """
        if k < 0:
            return 0
        re = set()
        have = set()
        for i in nums:
            if i-k in have:
                re.add(i-k)
            if i+k in have:
                re.add(i)
            have.add(i)
        print(re)
        return len(re)