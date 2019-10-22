# https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1120/
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a =  set(nums1).intersection(set(nums2))
        return 1
def test():
    s = Solution()
    assert not s.intersect([1,2,2,1], [2,2]) == [2,2]

    assert not s.intersect( nums1 = [4,9,5], nums2 = [9,4,9,8,4]) == [2,2]


if __name__ == "__main__":
    test()