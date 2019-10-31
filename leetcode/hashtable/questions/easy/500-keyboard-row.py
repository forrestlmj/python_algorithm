# https://leetcode.com/problems/keyboard-row/
import math


class Solution(object):
    d = dict()
    def make_dict(self,l1,v):
        for i in l1:
            self.d[i] = v
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l1,l2,l3 = "qwertyuiopQWERTYUIOP","asdfghjklASDFGHJKL","zxcvbnmZXCVBNM"
        # d = dict()
        self.make_dict(l1,-1)
        self.make_dict(l2,0)
        self.make_dict(l3,1)
        re = list()
        for word in words:
            v = self.d[word[0]]
            same_raw = True
            for k in word[1:]:
                if self.d[k] != v:
                    same_raw = False
                    break
            if same_raw:
                re.append(word)
        return re

def test():
    s = Solution()
    # s.countPrimes(10)
    assert s.findWords( ["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"]
    assert s.findWords( ["qaz","asxz"]) == []

    # assert s.countPrimes(11) == 5
    # assert s.countPrimes(12) == 5
    # assert s.findWords(0) == 0
    # assert s.countPrimes(1) == 0
    # assert s.countPrimes(2) == 0
    # assert s.countPrimes(3) == 1
    # assert s.countPrimes(4) == 2
    # assert s.countPrimes(5) == 2
    # assert s.countPrimes(23) == 8
if __name__ == "__main__":
    test()