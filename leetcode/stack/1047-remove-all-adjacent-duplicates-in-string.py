import queue
class Solution:
    def removeDuplicates(self, S: str) -> str:
        s = queue.deque()
        for i in S:
            if s:
                if i == s[-1]:
                    s.pop()
                else:
                    s.append(i)
            else:
                s.append(i)
        return "".join(s)