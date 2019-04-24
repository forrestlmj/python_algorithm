class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle.__len__() == 0:
            return 0
        else:
            l = int(haystack.__len__()/needle.__len__())
            if l < 1:
                return -1
            else:
                for i in range(len(haystack)-len(needle)+1):
                    t = haystack[i:i+len(needle)]
                    if t == needle:
                        return i
                return -1


def test():
    s = Solution()
    haystack = "hello"
    needle = "ll"
    assert s.strStr(haystack, needle) == 2
    haystack = "hello"
    needle = "lo"
    assert s.strStr(haystack, needle) == 3
    haystack = "hello"
    needle = "llo"
    assert s.strStr(haystack, needle) == 2
    haystack = "aaaaa"
    needle = "bba"
    assert s.strStr(haystack, needle) == -1
    haystack = "aaaaa"
    needle = "aaaaa"
    assert s.strStr(haystack, needle) == 0
    haystack = "aaaaa"
    needle = "aaaab"
    assert s.strStr(haystack, needle) == -1
if __name__ == "__main__":
    test()