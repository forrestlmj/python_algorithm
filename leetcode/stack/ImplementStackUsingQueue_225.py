class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = list()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.s.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.s.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.s[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.s) == 0
def test_0():
# Your MyStack object will be instantiated and called as such:
    obj = MyStack()
    obj.push(3)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()

if __name__ == "__main__":
    test_0()