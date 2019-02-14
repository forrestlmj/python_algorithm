# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isParentheses(self,a,b):
        parenthese = {"(": ")",
                      "[": "]",
                      "{": "}"}
        if a in parenthese.keys() and parenthese[a] == b:

            return True
        else:
            return False
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_l = [i for i in s]
        stack = []
        for i in s_l:
            if len(stack) == 0:
                stack.append(i)
            else:
                if self.isParentheses(stack[-1],i):
                    stack.pop()
                else:
                    stack.append(i)
        if len(stack) ==0:
            return True
        else:
            return False


def test():
    l1 = "()"
    l2 = "()[]{}"
    l3 = "(]"
    l4 = "([)]"
    l5 = "{[]}"
    s = Solution()
    assert s.isValid(l1) == True
    assert s.isValid(l2) == True
    assert s.isValid(l3) == False
    assert s.isValid(l4) == False
    assert s.isValid(l5) == True
def test_205512106():
    # https://leetcode.com/submissions/detail/205512106/
    l1 = "([)"
    s = Solution()
    assert s.isValid(l1) == False
test()
test_205512106()