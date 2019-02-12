# https://leetcode.com/problems/score-of-parentheses/
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

    def size(self):
        return len(self.stack)
class Solution(object):
    def is_int(self,x):
        return x not in ["(", ")"]
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = Stack()
        stack.push(S[0])
        S_l = [i for i in S]
        S_l.remove(S_l[0])
        while len(S_l) > 0 :
            # () = 1
            if not stack.isEmpty():
                if stack.top() == "(" and S_l[0] == ")":
                    stack.pop()
                    S_l.remove(S_l[0])
                    S_l.insert(0,1)
                    # stack.push(S_l[0])
                # AB = A+B case 1
                elif self.is_int(stack.top()) and self.is_int(S_l[0]):
                    A = stack.pop()
                    B = S_l[0]
                    S_l.remove(S_l[0])
                    S_l.insert(0,A+B)
                    # stack.push(S_l[0])
                # (A) = A*2
                elif self.is_int(stack.top()) and S_l[0] == ")":
                    A = stack.pop()
                    if stack.top() == "(":
                        stack.pop()
                        S_l.remove(S_l[0])
                        S_l.insert(0, A*2)
                        # stack.push(S_l[0])
                    else:
                        stack.push(A)
                else:
                    stack.push(S_l[0])
                    S_l.remove(S_l[0])
            # stack.push(S_l[0])
            # S_l.remove(S_l[0])
            else:
                stack.push(S_l[0])
                S_l.remove(S_l[0])

        if stack.size() == 1 and self.is_int(stack.top()):
            return stack.pop()

# TODO 思路:生成的答案插入到队列中
def test_0():
    s = Solution()
    S1 = "()"
    assert s.scoreOfParentheses(S1) == 1
    S2 = "(())"
    assert s.scoreOfParentheses(S2) == 2
    S3 = "()()"
    assert s.scoreOfParentheses(S3) == 2
    S4 = "(()(()))"
    assert s.scoreOfParentheses(S4) == 6

if __name__ == "__main__":
    test_0()