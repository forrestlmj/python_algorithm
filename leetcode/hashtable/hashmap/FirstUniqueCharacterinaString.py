# https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1120/
import sys
class Solution(object):
        def firstUniqChar(self, s):
            """
            :type s: str
            :rtype: int
            """
            d_dict = dict()
            # s = [i for i in s]
            for i in range(len(s)):
                if s[i] not in d_dict.keys():
                    d_dict[s[i]] = [i]
                else:
                    d_dict[s[i]].append(i)
            delete_key = []
            for k in d_dict.keys():
                if len(d_dict[k]) == 1:
                    d_dict[k] = d_dict[k][0]
                else:
                    delete_key.append(k)
            for k in delete_key:
                d_dict.pop(k)
            if len(d_dict) == 0:
                return -1
            l = sorted(d_dict.items(),key=lambda item:item[1])
            return l[0][1]
def test():
    s = Solution()
    assert  s.firstUniqChar("leetcode") == 0

    assert  s.firstUniqChar("loveleetcode") == 2
    assert  s.firstUniqChar("222211") == -1
    assert  s.firstUniqChar("1234") == 0
    assert  s.firstUniqChar("11111") == -1
    assert  s.firstUniqChar("22221") == 4


if __name__ == "__main__":
    test()