# https://leetcode.com/problems/two-sum/
# 数组求和
from random import randrange
class Solution:

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list1 = list()
        for i in nums:
            list1.append(i)
        for i in nums:
            complement = target - i
            if complement in list1 and list1.index(complement) != complement:
                return (list1.index(i), list1.index(complement))

def test_1(l, num):
    s = Solution()
    print(s.twoSum(l, num))
if __name__ == "__main__":
    l = [2, 7, 11, 15]
    # [3,2,4]
    # 6

    test_1(l, 9)