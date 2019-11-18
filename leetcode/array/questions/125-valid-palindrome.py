class Solution:
    def isPalindrome(self, s: str) -> bool:
        def inrange(s):
            return ("a"<=s<="z") or ("A"<=s<="Z") or ("0"<=s<="9")
        l,r = 0,len(s)-1
        while l<=r:
            if not inrange(s[l]):
                l += 1
                continue
            if not inrange(s[r]):
                r -= 1
                continue
            if s[l] == s[r] or (s[l] not in"0123456789" and s[r] not in "0123456789" and abs(ord(s[l])-ord(s[r]))==32):
                l += 1
                r -= 1
            else:
                return False
        return True
s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))

