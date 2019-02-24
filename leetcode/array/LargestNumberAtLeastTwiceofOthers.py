class Solution(object):

    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        max_index = nums.index(max_num)
        nums.remove(max_num)
        for i in nums:
            if max_num >= 2*i:
                pass
            else:
                return -1
        return max_index

def test_0():
    s = Solution()
    nums = [3, 6, 1, 0]
    assert s.dominantIndex(nums) == 1
    nums = [1]
    assert s.dominantIndex(nums) == 0
    nums = [1, 2, 3, 4]
    assert s.dominantIndex(nums) == -1

if __name__ == "__main__":
    test_0()
