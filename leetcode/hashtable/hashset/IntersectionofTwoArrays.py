# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1105/
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d_set = set()
        set_1 = set()
        set_2 = set()
        for i in nums1:
            set_1.add(i)
        for i in nums2:
            set_2.add(i)
        return set_1.intersection(set_2)

def test():
    s = Solution()
    assert s.intersection([1,2,2,1],[2,2]) == [2]
    assert s.intersection([4,9,5],[9,4,9,8,4]) == 4

if __name__ == "__main__":
    test()