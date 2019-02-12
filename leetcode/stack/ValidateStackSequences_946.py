# https://leetcode.com/problems/validate-stack-sequences/
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
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = Stack()
        re = True
        if len(pushed) == 0:
            return True
        stack.push(pushed[0])
        pushed.remove(pushed[0])
        while True:
            if (not stack.isEmpty()) and popped[0] == stack.top():
                stack.pop()
                popped.remove(popped[0])
            elif len(pushed)>0:
                stack.push(pushed[0])
                pushed.remove(pushed[0])
            else:
                break
        return stack.isEmpty()

def test_0():
    s = Solution()
    pushed = []
    popped = []
    assert s.validateStackSequences(pushed,popped) == True
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    assert s.validateStackSequences(pushed,popped) == True
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    assert s.validateStackSequences(pushed,popped) == False
# https://leetcode.com/submissions/detail/207338200/
def test_207338200():
    s = Solution()

    pushed =[4, 0, 1, 2, 3]
    popped = [4, 2, 3, 0, 1]
    assert s.validateStackSequences(pushed,popped) == False

if __name__ == "__main__":
    test_0()
    test_207338200()