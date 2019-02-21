# https://leetcode.com/problems/car-fleet/
class Solution(object):

    def carfleet_speed(self,car1,car2,target):
        # 0 为速度，1为位置
        if car1[1] == car2[1]:
            if car1[0] == car2[0]:
                return [car1[0], car1[1]]
            else:
                return False
        else:
            # 如果速度相差与距离相差符号相反，说明会相遇 and 相遇的时间小于等于辆车到达终点前的距离
            if (car1[0] - car2[0])*(car1[1] - car2[1]) < 0\
                    and abs((car1[0] - car2[0])/(car1[1] - car2[1])) <= min((target-car2[0])/car2[1],(target-car1[0])/car1[1]):
                return [ int(min(car1[0], car2[0])),int((abs(car1[1]-car2[1])/abs(car1[0]-car2[0]))*min(car1[0], car2[0])+max(car1[1],car2[1]))]
            else:
                return False

    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        if len(position) == 0 or len(speed) == 0 or len(speed) != len(position):
            return 0
        stack = []

        for car_id in range(len(speed)):
            if len(stack) == 0:
                stack.append([speed[car_id], position[car_id]])
            else:
                crash = self.carfleet_speed(stack[-1],[speed[car_id], position[car_id]],target)
                if crash:
                    # 相遇速度比之前的小，而且相遇时候的位置比之前远，进入栈
                    if crash[0] <= stack[-1][0]  and crash[1] >= stack[-1][1]:
                        stack.pop()
                        stack.append(crash)
                    else:
                        pass
                else:
                    stack.append([speed[car_id], position[car_id]])
        return len(stack)

def test_0():
    target = 12
    speed = [2, 4, 1, 1, 3]
    position = [10, 8, 0, 5, 3]
    output = 3
    s = Solution()
    assert s.carfleet_speed([2, 10], [4, 8], 12) == [2, 12]
    assert s.carfleet_speed([4, 8],[2, 10], 12) == [2, 12]

    assert s.carfleet_speed([1, 5], [3, 3], 12) == [1, 6]
    assert s.carfleet_speed([4, 10], [2, 8], 12) == False

    assert s.carFleet(target, position, speed) == output
def test_1():
    speed = []
    position = []
    target = 12
    s = Solution()
    assert s.carFleet(target, position, speed) == 0

if __name__ == "__main__":
    test_0()
    test_1()