# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1112/
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d_set = set()
        for i in nums:
            if i not in d_set:
                d_set.add(i)
            else:
                return True
        return False
def test():
    s = Solution()
    assert s.containsDuplicate([1,2,3,1]) == True
    assert s.containsDuplicate([1,2,3,4]) == False
    assert s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True

if __name__ == "__main__":
    test()