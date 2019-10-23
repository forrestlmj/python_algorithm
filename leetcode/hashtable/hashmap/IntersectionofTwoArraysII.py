# https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1120/
class Solution(object):
    def get_dict(self,nums):
        a = dict()
        for i in nums:
            if i not in a.keys():
                a[i] = 1
            else:
                a[i] += 1
        return a
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        注意这道题目的本意是找到两个集合中公共元素出现的最小次数
        """

        a = self.get_dict(nums1)
        b = self.get_dict(nums2)
        r = list()
        c = dict()
        for i in a.keys():
            if i in b.keys():
                c[i] = min(a[i],b[i])
        for i in c.keys():
            r +=[i]*c.get(i)
        return r
def test():
    s = Solution()
    assert s.intersect([1,2,2,1], [2,2]) == [2,2]

    assert s.intersect( nums1 = [4,9,5], nums2 = [9,4,9,8,4]) ==  [4,9]
    assert s.intersect(nums1=[1,2,2,2,1], nums2=[2,2,2]) == [2,2,2]

if __name__ == "__main__":
    test()