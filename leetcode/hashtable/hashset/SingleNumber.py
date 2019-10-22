# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1176/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d_set = set()
        for i in nums:
            if i not in d_set:
                d_set.add(i)
            else:
                d_set.remove(i)
            # nums.remove(i)
        return d_set.pop()
def test():
    s = Solution()
    assert s.singleNumber([2, 2, 1]) == 1
    assert s.singleNumber([4, 1, 2, 1, 2]) == 4
    assert s.singleNumber([1, 1, 1, 1, 2]) == 2
    # s.singleNumber([-1, -1, -2])
    assert s.singleNumber([-1, -1, -2]) == -2
if __name__ == "__main__":
    test()