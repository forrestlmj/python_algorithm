# https://leetcode.com/problems/next-greater-element-i/
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0 or len(findNums) == 0:
            return []
        n = dict()
        for index in range(len(nums)-1):
            if nums[index] < nums[index+1]:
                n[nums[index]] = nums[index+1]
            else:
                find = False
                for j_index in range(index+1, len(nums)):
                    if nums[index] < nums[j_index]:
                        n[nums[index]] = nums[j_index]
                        find = True
                        break
                if not find:
                    n[nums[index]] = -1
        n[nums[-1]] = -1
        return [n[i] for i in findNums]


def test_0():
    s = Solution()
    f = [4, 1, 2]
    n = [1, 3, 4, 2]
    assert s.nextGreaterElement(f, n) == [-1, 3, -1]
    f = [2, 4]
    n = [1, 2, 3, 4]
    assert s.nextGreaterElement(f, n) == [3, -1]
    f = [4, 1, 2]
    n = [1, 3, 4, 2, 5]
    assert s.nextGreaterElement(f, n) == [5, 3, 5]
    f = [1]
    n = [1]
    assert s.nextGreaterElement(f, n) == [-1]
    f = [1]
    n = [-1, 1, -100]
    assert s.nextGreaterElement(f, n) == [-1]
    f = []
    n = []
    assert s.nextGreaterElement(f, n) == []
    f = []
    n = [1,2,3]
    assert s.nextGreaterElement(f, n) == []
    f = [1,2,3]
    n = [1,2,3]
    assert s.nextGreaterElement(f, n) == [2,3,-1]
    f = [2,3]
    n = [1,2,3]
    assert s.nextGreaterElement(f, n) == [3,-1]
    f = [3,2]
    n = [1,2,3]
    assert s.nextGreaterElement(f, n) == [-1,3]
if __name__ == "__main__":
    test_0()
    # TODO 使用栈解法
    # https://leetcode.com/problems/next-greater-element-i/discuss/97595/Java-10-lines-linear-time-complexity-O(n)-with-explanation
