#https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1121/
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d_dict = dict()
        for i in range(len(nums)):
            if nums[i] not in d_dict.keys():
                d_dict[nums[i]] = [i]
            else:
                d_dict[nums[i]].append(i)
        for i in d_dict.keys():
            if len(d_dict.get(i))>1:
                for j in range(1,len(d_dict.get(i))):
                    if d_dict.get(i)[j] - d_dict.get(i)[j-1] <= k:
                        return True
                    else:
                        pass
            else:
                pass
        return False

def test():
    s = Solution()
    assert s.containsNearbyDuplicate(nums = [1,2,3,1], k = 3) == True
    assert s.containsNearbyDuplicate(nums = [1,0,1,1], k = 1) == True
    assert s.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2) == False
    assert s.containsNearbyDuplicate(nums = [1], k = 1) == False
    assert s.containsNearbyDuplicate(nums = [1], k = 3) == False
    assert s.containsNearbyDuplicate(nums = [1,2], k = 1) == False
    assert s.containsNearbyDuplicate(nums = [1,2,2,2,1], k = 1) == True
    assert s.containsNearbyDuplicate(nums = [1,2,3,4,1,11,1,11], k = 2) == True

if __name__ == "__main__":
    test()