# https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1133/
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        f_dict = dict()
        for i in nums:
            if i not in f_dict.keys():
                f_dict[i] = 1
            else:
                f_dict[i] += 1
        l = sorted(f_dict.items(),key=lambda _:_[1],reverse=True)

        return [l[i][0] for i in range(k)]

def test():
    s = Solution()
    assert s.topKFrequent(   nums = [1,1,1,2,2,3], k = 2) == [1,2]
    # #
    assert s.topKFrequent( nums = [1], k = 1) == [1]

if __name__ == "__main__":
    test()