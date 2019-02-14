# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = list()
        for i in S:
            if i == "(":
                stack.append(i)
            if i == ")":
                if len(stack)>0:
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        stack.append(i)
                else:
                    stack.append(i)
        return len(stack)

def test_0():
    s = Solution()
    S = "())"
    assert s.minAddToMakeValid(S) == 1
    S = "((("
    assert s.minAddToMakeValid(S) == 3
    S = "()"
    assert s.minAddToMakeValid(S) == 0
    S = "()))(("
    assert s.minAddToMakeValid(S) == 4
if __name__ == "__main__":
    test_0()
