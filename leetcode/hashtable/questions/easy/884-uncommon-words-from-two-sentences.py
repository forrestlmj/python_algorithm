# https://leetcode.com/problems/keyboard-row/
import math


class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a_dict, b_dict = dict(), dict()
        for word in A.split(" "):
            if word not in a_dict:
                a_dict[word] = 1
            else:
                a_dict[word] += 1
        for word in B.split(" "):
            if word not in b_dict:
                b_dict[word] = 1
            else:
                b_dict[word] += 1


        # a_key = set(a_dict.keys())
        # for k in a_key:
        #     if a_dict[k] > 1:
        #         a_dict.pop(k)
        # b_key = set(b_dict.keys())
        #
        # for k in b_key:
        #     if b_dict[k] > 1:
        #         b_dict.pop(k)
        intersection = set(a_dict.keys()).intersection(set(b_dict.keys()))
        re = list()
        for k in a_dict.keys():
            if k not in intersection and a_dict[k] == 1:
                re.append(k)
        for k in b_dict.keys():
            if k not in intersection and b_dict[k] == 1:
                re.append(k)
        return re
def test():
    s = Solution()
    assert s.uncommonFromSentences(A = "this apple is sweet", B = "this apple is sour") == ["sweet","sour"]
    assert s.uncommonFromSentences( A = "apple apple", B = "banana") == ["banana"]
    assert s.uncommonFromSentences( A = "s z z z s", B = "s z ejt") == ["ejt"]





if __name__ == "__main__":
    test()