#https://leetcode-cn.com/explore/learn/card/binary-search/208/background/833/
class Solution:
    def search(self, nums: [int], target: int) -> int:
        l,r = 0,len(nums)-1
        mid = -1
        while(l<=r):
            mid = int((l+r)/2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid-1
            elif target > nums[mid]:
                l = mid+1
        return -1
s = Solution()
s.search( nums = [-1,0,3,5,9,12], target = 2)