# https://leetcode.com/problems/unique-number-of-occurrences/
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count_dict = dict()
        for i in arr:
            if i not in count_dict.keys():
                count_dict[i] = 1
            else:
                count_dict[i] += 1

        return len(set(count_dict.values())) == len(count_dict)

def test():
    s = Solution()
    assert s.uniqueOccurrences([1]) == True
    assert s.uniqueOccurrences([1,2,2,1,1,3]) == True
    assert s.uniqueOccurrences(arr = [1,2]) == False
    assert s.uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]) == True

    print("ok")

if __name__ == "__main__":
    test()