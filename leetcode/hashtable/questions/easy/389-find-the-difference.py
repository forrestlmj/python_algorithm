# https://leetcode.com/problems/find-the-difference/
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_count = dict()
        for i in s:
            if i not in s_count.keys():
                s_count[i] = 1
            else:
                s_count[i] += 1
        for i in t:
            if i not in s_count.keys():
                return i
            else:
                if s_count[i] == 0:
                    return i
                else:
                    s_count[i] -= 1

def test():
    s = Solution()
    assert s.findTheDifference( s = "abcd", t = "abcde") == "e"
    assert s.findTheDifference( s = "abcc", t = "abcce") == "e"
    assert s.findTheDifference( s = "a", t = "aa") == "a"
    assert s.findTheDifference( s = "sdfse", t = "sedfss") == "s"
    #
    # assert s.getHint( secret = "1807", guess = "7810") == "1A3B"
    # assert s.getHint( secret = "1123", guess = "0111") == "1A1B"
# def test1():
#     s = Solution()
#     assert s.getHint( secret = "1122", guess = "2211") == "0A4B"
# def test2():
#     s = Solution()
#     assert s.getHint( secret = "11", guess = "10") == "1A0B"
# def test3():
#     s = Solution()
#
#     assert s.getHint( secret = "11122", guess = "22311") == "0A4B"

if __name__ == "__main__":
    test()
    # test1()
    # test2()
    # test3()