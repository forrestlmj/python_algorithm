# https://leetcode.com/problems/backspace-string-compare/
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        Stack_S = list()
        Stack_T = list()
        for i in S:
            if i == "#":
                if len(Stack_S)>0:
                    Stack_S.pop()
                else:
                    pass
            else:
                Stack_S.append(i)
        for i in T:
            if i == "#":
                if len(Stack_T)>0:
                    Stack_T.pop()
                else:
                    pass
            else:
                Stack_T.append(i)
        return Stack_S == Stack_T
def test_0():
    s = Solution()
    S = "ab#c"
    T = "ad#c"
    assert s.backspaceCompare(S,T) == True
    S = "ab##"
    T = "c#d#"
    assert s.backspaceCompare(S,T) == True
    S = "a##c"
    T = "#a#c"
    assert s.backspaceCompare(S,T) == True
    S = "a#c"
    T = "b"
    assert s.backspaceCompare(S,T) == False
    S = ""
    T = "#######"
    assert s.backspaceCompare(S,T) == True
