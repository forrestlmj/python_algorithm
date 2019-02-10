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
            if complement in list1 and list1.index(i) != list1.index(complement) :
                    # and list1.index(i) != list1.index(complement):
                return [list1.index(i), list1.index(complement)]
            elif complement == target/2 and nums.count(complement) == 2:
                return [nums.index(complement,0),nums.index(i,nums.index(complement,0)+1)]


def test_1():
    l = [2, 7, 11, 15]
    num = 9
    s = Solution()
    assert s.twoSum(l, num) == [0,1]

def test_193657691():
    # https://leetcode.com/submissions/detail/193657691/
    s = Solution()
    t1 = [3,2,4]
    assert s.twoSum(t1,6) == [1,2]
def test_206442980():
    # https://leetcode.com/submissions/detail/206442980/
    s = Solution()
    t1 = [3,3]
    assert s.twoSum(t1,6) == [0,1]
def test_206453420():
    s = Solution()
    t1 = [2,5,5,11]
    assert s.twoSum(t1,10) == [1,2]
    # https://leetcode.com/submissions/detail/206453420/
if __name__ == "__main__":
    # test_1()
    test_193657691()
    test_206442980()
    test_206453420()