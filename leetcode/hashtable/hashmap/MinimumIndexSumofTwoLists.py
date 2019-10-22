#https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1177/
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        set_r= dict()
        set_1 = dict()
        set_2 = dict()

        for i in range(len(list1)):
            set_1[list1[i]] = i
        for i in range(len(list2)):
            set_2[list2[i]] = i
        for k in (set(set_1.keys()).intersection(set(set_2.keys()))):
            set_r[k] = set_1[k]+set_2[k]


        minsum = min(set_r.values())
        l = sorted(set_r.items(),key=lambda item:item[1])
        re = []
        for (k,v) in l:
            if v==minsum:
               re.append(k)
            else:
                break
        return re
def test():
    s = Solution()
    assert s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"]
, ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]) ==  ["Shogun"]
    assert s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"]
, ["KFC", "Shogun", "Burger King"]
) == ["Shogun"]
    assert s.findRestaurant(["aa","bb"], ["aa","bb"]) == ["aa"]
    print(s.findRestaurant(["aa","bb"], ["bb","aa"]))
    # assert s.findRestaurant(["aa","bb"], ["bb","aa"]) == ["aa"]

if __name__ == "__main__":
    test()