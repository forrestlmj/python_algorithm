# https://leetcode.com/problems/min-stack/
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = list()
        self.min = float('inf')

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x < self.min:
            self.min = x
        self.s.append(x)
    def pop(self):
        """
        :rtype: void
        """
        if len(self.s) > 0:
            if self.s[-1] < self.min:
                self.min = self.s[-1]
            self.s.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.s) > 0:
            return self.s[-1]

    def getMin(self):
        """
        :rtype: int
        """
        min = float('inf')
        for i in self.s:
            if i < min:
                min = i
        return min

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
def test_0():

    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2
if __name__ == "__main__":
    test_0()
