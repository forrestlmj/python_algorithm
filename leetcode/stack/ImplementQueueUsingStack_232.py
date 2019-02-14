# https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = list()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.q.append(x)
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """

        if not self.empty():
            a = self.q[0]
            self.q.remove(a)
            return a

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.empty():
            return self.q[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.q) == 0
def test_0():
# Your MyQueue object will be instantiated and called as such:
    obj = MyQueue()
    obj.push(3)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
if __name__ == "__main__":
    test_0()