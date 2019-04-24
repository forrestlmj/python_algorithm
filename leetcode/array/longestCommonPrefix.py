import sys
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        re = ""
        min_size, min_str = sys.maxsize, ""
        for i in strs:
            if len(i) < min_size:
                min_str, min_size = i, len(i)
        # print(min_str)
        for i in range(len(min_str)):
            for str in strs:
                if str[i] == min_str[i]:
                    pass
                else:
                    print(re)
                    return re
            re += min_str[i]
        return re
def test_0():
    s = Solution()
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
    assert s.longestCommonPrefix([]) == ""

if __name__ == "__main__":
    test_0()
