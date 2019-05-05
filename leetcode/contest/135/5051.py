class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        a = [points[1][0]-points[0][0],points[1][1]-points[0][1]]
        b = [points[2][0]-points[1][0],points[2][1]-points[1][1]]
        print(a[0]*b[1]==a[1]*b[0])
        return not a[0]*b[1]==a[1]*b[0]
def test_0():
    s = Solution()
    a, b, c = 1, 2, 5
    assert s.isBoomerang([[1,1],[2,3],[3,2]]) == True
    a, b, c = 4, 3, 2
    assert s.isBoomerang( [[1,1],[2,2],[3,3]]) == False

if __name__ == "__main__":
    test_0()