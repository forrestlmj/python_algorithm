import sys


class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr = sorted(arr)
        # print(arr)
        min_gap = sys.maxsize
        gap = list()

        for i in range(1,len(arr)):
            cur_gap = arr[i] - arr[i-1]
            if cur_gap < min_gap:
                min_gap = cur_gap
                gap = list()
                gap.append([arr[i-1],arr[i]])
            elif cur_gap == min_gap:
                gap.append([arr[i-1],arr[i]])
        return gap
s = Solution()
print(s.minimumAbsDifference(arr = [4,2]))

print(s.minimumAbsDifference(arr = [4,2,1,3]))
print(s.minimumAbsDifference(arr = [1,3,6,10,15]))
print(s.minimumAbsDifference(arr = [3,8,-10,23,19,-4,-14,27]))
