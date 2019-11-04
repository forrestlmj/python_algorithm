class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        not_in_arr1_l = list()
        count = dict()

        for i in arr1:
            if i not in arr2:
                not_in_arr1_l.append(i)
            else:
                if i not in count:
                    count[i] = 1
                else:
                    count[i] += 1
        a = list()
        for i in arr2:
            if i in count:
                a += [i]*count[i]
        a += sorted(not_in_arr1_l)
        return a
s = Solution()
print(s.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
print(s.relativeSortArray(arr1 = [2,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
print(s.relativeSortArray(arr1 = [100,100,0,2,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
