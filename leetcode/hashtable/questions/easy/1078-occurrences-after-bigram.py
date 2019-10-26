# https://leetcode.com/problems/find-common-characters/
import sys


class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        text = text.split(" ")
        # print(text)
        d = dict()
        for index in range(len(text)):
            if text[index] not in d:
                d[text[index]] = [index]
            else:
                d[text[index]].append(index)
        f, s = d[first], d[second]
        re = list()
        for i in s:
            if i-1 in f and i+1<len(text):
                re.append(text[i+1])
        return re

def test():
    """

    :return:
    """
    s = Solution()
    # assert \
    s.findOcurrences( text = "alice is a good girl she is a good student", first = "a", second = "good") \
           # ==  ["e","l","l"]
    # assert \
    s.findOcurrences( text = "we will we will rock you", first = "we", second = "will") \
           # == ["c","o"]
    s.findOcurrences( text = "alice is a good girl she is a good student", first = "good", second = "student")
    s.findOcurrences( text = "alice is a good girl she is a good student", first = "alice", second = "student")

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