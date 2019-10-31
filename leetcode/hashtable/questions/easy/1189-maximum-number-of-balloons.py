# https://leetcode.com/problems/keyboard-row/
import math


class Solution:
    def maxNumberOfBalloons(self, text):
        c = "balloon"
        d = {
            "b":0,
            "a":0,
            "l":0,
            "o":0,
            "n":0
        }
        for i in text:
            if i in d:
                d[i] += 1
        return min(d["b"],d["a"],d["n"],int(d["l"]/2),int(d["o"]/2))





def test():
    s = Solution()
    # s.countPrimes(10)
    assert s.maxNumberOfBalloons(text = "nlaebolko") == 1
    assert s.maxNumberOfBalloons( text = "loonbalxballpoon") == 2
    assert s.maxNumberOfBalloons( text = "leetcode") == 0

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