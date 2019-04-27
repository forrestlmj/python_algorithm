class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return sum(sorted(nums)[::2])

def test():
    l = [1, 4, 3, 2]
    s = Solution()
    assert s.arrayPairSum(l)==4


if __name__ == "__main__":
    test()
