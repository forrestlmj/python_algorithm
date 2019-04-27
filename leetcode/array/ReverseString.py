class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s)-1
        if i == j:
            return []
        while(i<j):
            t1 = s[i]
            t2 = s[j]
            s[i] = t2
            s[j] = t1
            i+=1
            j-=1
        return s
def test():
    s = Solution()
    l = ["h","e","l","l","o"]
    assert s.reverseString(l) == ["o","l","l","e","h"]
    l2 = ["H","a","n","n","a","h"]
    assert s.reverseString(l2) == ["h","a","n","n","a","H"]


if __name__ == "__main__":
    test()