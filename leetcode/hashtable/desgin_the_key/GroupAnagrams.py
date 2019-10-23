#https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1124/
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d_dict = dict()
        for i in strs:
            k = "".join(sorted(i,key=lambda _:_))
            if k not in d_dict:
                d_dict[k] = [i]
            else:
                d_dict[k].append(i)
        return d_dict.values()
def test():
    s = Solution()
    assert not s.groupAnagrams( ["eat", "tea", "tan", "ate", "nat", "bat"]) ==[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]



if __name__ == "__main__":
    test()