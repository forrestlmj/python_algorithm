# https://leetcode.com/problems/valid-anagram/
class Solution(object):
    def get_dict(self,s):
        s_d = dict()
        for i in s:
            if i not in s_d.keys():
                s_d[i] = 1
            else:
                s_d[i] += 1
        return s_d
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.get_dict(s) == self.get_dict(t)

def test():
    s = Solution()
    assert s.isAnagram(s = "anagram", t = "nagaram") == True
    assert s.isAnagram( s = "rat", t = "car") == False
    assert s.isAnagram( s = "", t = "") == True
    print("ok")

if __name__ == "__main__":
    test()
