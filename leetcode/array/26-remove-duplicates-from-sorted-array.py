class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        if nums is None or len(nums) ==0:
            return 0
        pre = nums[0]
        for i in nums[1:]:
            if i == pre:
                nums.remove(pre)
            else:
                pre = i
                count+=1
        return count
def test0():
    """
    本题考察的是的双指针问题，注意对于输入要考虑None与list情况。
    :return: 
    """
    s = Solution()
    nums = [1, 1, 2]
    assert s.removeDuplicates(nums) == 2
    nums =  [0,0,1,1,1,2,2,3,3,4]
    assert s.removeDuplicates(nums) == 5
    nums = None
    assert s.removeDuplicates(nums) == 0
    nums = []
    assert s.removeDuplicates(nums) == 0


if __name__ == "__main__":
    test0()