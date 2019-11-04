# https://leetcode.com/problems/count-primes/
import math


class Solution(object):
    d = dict()
    def isALessThenB(self,a,b):
        i = 0
        while i< min(len(a),len(b)):
            if self.d[a[i]] > self.d[b[i]]:
                return False
            elif self.d[a[i]] < self.d[b[i]]:
                return True
            i +=1
        if i == min(len(a),len(b)):
            return len(a) <= len(b)
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
            """
        for i in range(len(order)):
            self.d[order[i]] = i
        for i in range(1,len(words)):
            if not self.isALessThenB(words[i-1],words[i]):
                return False
        return True

def test():
    s = Solution()
    assert s.isAlienSorted(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz") == True

    assert s.isAlienSorted( words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz") == False
    assert s.isAlienSorted(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz") == False
    assert s.isAlienSorted(words = ["hello"], order = "hlabcdefgijkmnopqrstuvwxyz") == True
    assert s.isAlienSorted(words = ["hello","hello"], order = "hlabcdefgijkmnopqrstuvwxyz") == True
    assert s.isAlienSorted(["ubg","kwh"],"qcipyamwvdjtesbghlorufnkzx") == True

if __name__ == "__main__":
    test()