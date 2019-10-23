# https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1135/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp_count = 0
        max_len = 0
        seen_location = dict()
        for i in range(len(s)):
            tmp_count += 1
            if s[i] in seen_location:
                tmp_count = min(i - seen_location[s[i]],tmp_count)
            seen_location[s[i]] = i
            if max_len < tmp_count:
                max_len = tmp_count
        return max_len
def test():
    s = Solution()
    assert s.lengthOfLongestSubstring(  "pwwkew") == 3
    # #
    assert s.lengthOfLongestSubstring( "abcabcbb") == 3
    assert s.lengthOfLongestSubstring( "abcabcd") == 4
    #
    assert  s.lengthOfLongestSubstring( "bbbbb") == 1
    assert s.lengthOfLongestSubstring(  "abc") == 3
    assert s.lengthOfLongestSubstring(  "") == 0
    assert s.lengthOfLongestSubstring(  "abba") == 2
    assert s.lengthOfLongestSubstring(  "tmmzuxt") == 5


""
if __name__ == "__main__":
    test()