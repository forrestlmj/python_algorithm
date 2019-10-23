# https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1136/
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        stone_dict = dict()
        for s in S:
            if s not in stone_dict:
                stone_dict[s] = 1
            else:
                stone_dict[s] += 1
        count = 0
        for j in J:
            if j in stone_dict.keys():
                count+=stone_dict[j]
        return count
def test():
    s = Solution()
    assert  s.numJewelsInStones( J = "aA", S = "aAAbbbb") == 3
    assert  s.numJewelsInStones( J = "z", S = "ZZ") == 0
    assert  s.numJewelsInStones( J = "z", S = "") == 0
    assert  s.numJewelsInStones( J = "", S = "") == 0
    assert  s.numJewelsInStones( J = "", S = "zz") == 0


if __name__ == "__main__":
    test()