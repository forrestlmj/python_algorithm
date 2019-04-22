class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        s = list()
        l = sorted(costs,key=lambda l:l[0])
        r = sorted(costs,key=lambda l:l[1])
        print(l)
        print(r)

        # for i in costs:
        #     if len(s) == 0:
        #         s.append(i)
        #     else:
        #         while(len(s)>0 and len(s) <= len(costs)/2):
        #             if(sum(s[:-2][0])+s[-1][0]>i[0] and s[-1][1] <i[1]):
        #                 s.pop()
        #             else:
        #                 break
        #         s.append(i)


        # print(r)
def test_0():
    s = Solution()
    s.twoCitySchedCost( [[30,200],[400,50],[10,20],[30,20]])

    # s.twoCitySchedCost( [[10,20],[30,200],[400,50],[30,20]])
if __name__ == "__main__":
    test_0()