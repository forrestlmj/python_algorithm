class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        elif len(nums) < 2:
            return 0
        for index in range(0, len(nums)):
            if sum(nums[:index]) == sum(nums[index+1:]):
                return index
        return -1

def test_0():
    nums = [1, 7, 3, 6, 5, 6]
    s = Solution()
    assert s.pivotIndex(nums) == 3
    nums = [1 ,2, 3]
    assert s.pivotIndex(nums) == -1
    nums = [-1,-1,-1,0,1,1]
    assert s.pivotIndex(nums) == 0
    nums = [-1,0]
    assert s.pivotIndex(nums) == 0
    nums = [0]
    assert s.pivotIndex(nums) == 0
    nums = []
    assert s.pivotIndex(nums) == -1

if __name__ == "__main__":
    test_0()
