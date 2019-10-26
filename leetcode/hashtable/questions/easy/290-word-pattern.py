# https://leetcode.com/problems/word-pattern/
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        l = str.split(" ")
        if len(l) != len(pattern):
            return False
        map = dict()
        for i in range(len(pattern)):
            if pattern[i] not in map.keys():
                if l[i] not in map.values():
                    map[pattern[i]] = l[i]
                else:
                    return False
            if pattern[i] in map.keys():
                if l[i] != map[pattern[i]]:
                    return False
        return True
def test():
    s = Solution()
    assert s.wordPattern(  pattern = "abba", str = "dog cat cat dog") == True
    assert s.wordPattern( pattern = "abba", str = "dog cat cat fish") == False
    assert s.wordPattern( pattern = "aaaa", str = "dog cat cat dog") == False
    assert s.wordPattern( pattern = "abba", str = "dog dog dog dog") == False
    assert s.wordPattern(  pattern = "a", str = "dog") == True
    assert s.wordPattern(  pattern = "ab", str = "dog x") == True
    assert s.wordPattern(  pattern = "abb", str = "dog x z") == False
    assert s.wordPattern(  pattern = "aaa", str = "aa aa aa aa") == False
    assert s.wordPattern(  pattern = "aaaaaa", str = "aa aa aa aa") == False

#
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