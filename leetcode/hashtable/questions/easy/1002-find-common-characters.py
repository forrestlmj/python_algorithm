# https://leetcode.com/problems/find-common-characters/
import sys


class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        min_dict = dict()
        for k in map(chr,range(97,123)):
            min_dict[k] = sys.maxsize
        for a in A:
            cu_dict = dict()
            for ch in a:
                if ch not in cu_dict:
                    cu_dict[ch] = 1
                else:
                    cu_dict[ch] += 1
            ks = set(min_dict.keys())
            for k in ks:
                if k not in cu_dict:
                    min_dict.pop(k)
                else:
                    if cu_dict[k] < min_dict[k]:
                        min_dict[k] = cu_dict[k]
            a = 1
        r = list()
        for (k,v) in min_dict.items():
            r += [k for _ in range(v)]

        return r
def test():
    """

    :return:
    """
    s = Solution()
    # assert \
    s.commonChars(["bella","label","roller"]) \
           # ==  ["e","l","l"]
    # assert \
    s.commonChars( ["cool","lock","cook"]) \
           # == ["c","o"]

    # assert s.countCharacters( words = ["hello","world","leetcode"], chars = "welldonehoneyr") == 10
    # assert s.countCharacters( s = "a", t = "aa") == "a"
    # assert s.findTheDifference( s = "sdfse", t = "sedfss") == "s"
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