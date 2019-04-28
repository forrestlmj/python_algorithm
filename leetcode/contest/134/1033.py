class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        a,b,c = sorted([a,b,c])

        if b == a+1 and c==b+1:
            return [0, 0]
        elif (b == a+1 and c!=b+1 ) or ( b!= a+1 and c== b+1):
            return [1, max(c-b,b-a)-1]
        elif (b == a + 2) or(c == b+2):
            return [1,c-b+b-a-2]
        else:
            return [2, c-b+b-a-2]


def test_0():
    s = Solution()
    a, b, c = 1, 2, 5
    assert s.numMovesStones(a,b,c) == [1,2]
    a, b, c = 4, 3, 2
    assert s.numMovesStones(a,b,c) == [0,0]
    a ,b, c = 2,4,1
    assert s.numMovesStones(a,b,c) == [1,1]
    a ,b, c = 3,5,1
    assert s.numMovesStones(a,b,c) == [1,2]
    a ,b, c = 3,6,1
    assert s.numMovesStones(a,b,c) == [1,3]
if __name__ == "__main__":
    test_0()