class Solution:
    def findErrorNums(self, nums: [int]) -> [int]:
        """
        bitmap解法，时间空间复杂度O(N)
        :param nums:
        :return:
        """
        a,b = -1,-1
        l = [False] * len(nums)
        for i in nums:
            if not l[i-1]:
                l[i-1] = True
            else:
                a = i
        for i in range(0,len(l)):
            if not l[i]:
                b = i+1
        return [a,b]