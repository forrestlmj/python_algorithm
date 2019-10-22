# https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1117/
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_d = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in dict_d:
                if t[i] in dict_d.values():
                    return False
                dict_d[s[i]] = t[i]

                    # if t[i] not in dict_d.keys():
                #     dict_d[t[i]] = s[i]
                # else:
                #     if dict_d[t[i]] != t[i]:
                #         return False
                #     else:
                #         pass
            else:
                if dict_d[s[i]] != t[i]:
                    return False
                else:
                    pass
        return True
def test():
    s = Solution()
    assert s.isIsomorphic("a", "aa") == False

    assert s.isIsomorphic("egg", "add") == True
    assert s.isIsomorphic("foo", "bar") == False
    assert s.isIsomorphic("paper", "title") == True
    assert s.isIsomorphic("aabb", "aass") == True
    assert s.isIsomorphic("aabb", "adss") == False
    assert s.isIsomorphic("a", "d") == True
    assert s.isIsomorphic("a", "a") == True
    assert s.isIsomorphic("ab", "aa") == False

if __name__ == "__main__":
    test()