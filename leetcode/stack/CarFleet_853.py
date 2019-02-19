# https://leetcode.com/problems/car-fleet/
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        return 3

def test_0():
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    output = 3
    s = Solution()
    assert s.carFleet(target, position, speed) == output
