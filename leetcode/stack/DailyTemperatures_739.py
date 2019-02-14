# https://leetcode.com/problems/daily-temperatures/
class Stack(object):
    def __init__(self):
        self.stack = list()
    def isEmpty(self):
        return len(self.stack) == 0
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
    def top(self):
        if not self.isEmpty():
            return self.stack[-1]
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        o = [0 for i in range(len(T))]
        # o[0] = 0
        stack = Stack()

        re_T = list(reversed(T))
        stack.push((re_T[0], 0))
        for index in range(1, len(re_T)):
            gap_count_day = 0
            while not stack.isEmpty() and stack.top()[0] <= re_T[index]:
                # stack.pop()
                gap_count_day=gap_count_day+stack.pop()[1]
            if stack.isEmpty():
                stack.push((re_T[index],0))
                o[index] = 0
            else:
                gap_count_day+=1
                stack.push((re_T[index],gap_count_day))
                o[index] = gap_count_day
        return list(reversed(o))

def test_0():
    s = Solution()
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    assert s.dailyTemperatures(T) == [1, 1, 4, 2, 1, 1, 0, 0]
    T = [100,73,74,100]
    assert s.dailyTemperatures(T) == [0,1,1,0]
    T = [88,88,88]
    assert s.dailyTemperatures(T) == [0,0,0]
    T = [100]
    assert s.dailyTemperatures(T) == [0]
    T = [77,77,77,100]
    assert s.dailyTemperatures(T) == [3,2,1,0]

if __name__ == "__main__":
    test_0()