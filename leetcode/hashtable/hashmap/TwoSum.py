# https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1115/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d_dict = dict()

        for i in range(len(nums)):
            if target - nums[i] not in d_dict.keys():
                d_dict[nums[i]] = i
            else:
                # if target - nums[i] == nums[i]:
                return [d_dict[target-nums[i]],i]
                # else:
                #     return [d_dict[target-nums[i]],i]

def test():
    s = Solution()
    assert s.twoSum([2, 7, 11, 15],9) == [0,1]
    assert s.twoSum([2, 7, 11, 15],26) == [2,3]
    assert s.twoSum([3, 3],6) == [0,1]

    assert s.twoSum([3, 6, 3, 15],6) == [0,2]

if __name__ == "__main__":
    test()