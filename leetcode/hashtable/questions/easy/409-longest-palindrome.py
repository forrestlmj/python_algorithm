# https://leetcode.com/problems/find-the-difference/
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        is_odd = dict()
        count = 0
        for i in s:
            if i not in is_odd.keys():
                is_odd[i] = 1
            else:
                is_odd[i] = (is_odd[i]+1)%2
                if is_odd[i] == 0:
                    count = count+2
                else:
                    pass
        a =1 if max(is_odd.values())>0 else 0
        return a+count


def test():
    s = Solution()
    assert s.longestPalindrome( "abccccdd") == 7
    # assert s.longestPalindrome( s = "abcc", t = "abcce") == "e"
    # assert s.longestPalindrome( s = "a", t = "aa") == "a"
    # assert s.longestPalindrome( s = "sdfse", t = "sedfss") == "s"
    assert s.longestPalindrome( "aaabbbbb") == 7 #   bababab
    assert s.longestPalindrome( "aaaabbbbb") == 9 #   bababab
    assert s.longestPalindrome( "aaacccbbbbb") == 9 #   bababab

    # assert s.longestPalindrome( "aaabbbbbccccc") == 7 # acbcbcbcbca
    assert s.longestPalindrome("abcd") == 1
if __name__ == "__main__":
    test()
