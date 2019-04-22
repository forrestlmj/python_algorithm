class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        re = list()
        for i in range(R):
            for j in range(C):
                dis = abs(r0-i)+abs(c0-j)
                re.append(([i,j],dis))
        a = sorted(re, key=lambda l: l[1])
        print(a)
        l = [i[0] for i in a]
        print(l)
        return l
def test_0():
    s = Solution()
    s.allCellsDistOrder(1,2,0,0)
    s.allCellsDistOrder(2,2,0,1)
    s.allCellsDistOrder(2,3,1,2)
if __name__ == "__main__":
    test_0()