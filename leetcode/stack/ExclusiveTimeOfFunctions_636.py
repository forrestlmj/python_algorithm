# https://leetcode.com/problems/exclusive-time-of-functions/
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

# Given the running logs of n functions that are executed in a nonpreemptive
#  single threaded CPU, find the exclusive time of these functions.
# 非抢占式cpu,因此不会出现连续两个不同进程start的log情况出现
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        eTime = [0 for i in range(n)]
        stack = Stack()
        l = logs[0].split(":")
        l[0] = int(l[0])
        l[2] = int(l[2])
        stack.push(l)
        sum_gap = 0
        for log in logs[1:]:
            l = log.split(":")
            l[0] = int(l[0])
            l[2] = int(l[2])
            if stack.isEmpty():
                stack.push(l)

            elif stack.top()[0] == l[0] and stack.top()[1] == "start" and l[1] == "end":
                start = stack.pop()
                gap = l[2] - int(start[2]) + 1
                sum_gap += gap
                eTime[start[0]] = eTime[start[0]] + gap
                if not stack.isEmpty():
                    p = stack.pop()
                    p[2] = p[2] + sum_gap
                    stack.push(p)
            else:
                # l[2] = l[2] - sum_gap
                stack.push(l)
        return eTime


def test_0():
    n = 2
    logs = ["0:start:0",
           "1:start:2",
           "1:end:5",
           "0:end:6"]
    s = Solution()
    assert s.exclusiveTime(n, logs) == [3, 4]

    # n = 3
    # logs = ["0:start:0",
    #        "1:start:2",
    #        "1:end:5",
    #        "2:start:7",
    #         "2:end:10",
    #         "0:end:12"]
    # s = Solution()
    # assert s.exclusiveTime(n, logs) == [5, 4,4]
#https://leetcode.com/submissions/detail/207655800/
def test_207655800():
    n = 3
    logs = ["0:start:0", "0:end:0", "1:start:1", "1:end:1", "2:start:2", "2:end:2", "2:start:3", "2:end:3"]
    s = Solution()
    assert s.exclusiveTime(n, logs) == [1, 1,2]
# https://leetcode.com/submissions/detail/207656499/
def test_207656499():
    n =1
    logs =["0:start:0","0:start:1","0:start:2","0:end:3","0:end:4","0:end:5"]
    s = Solution()
    s.exclusiveTime(n, logs)
if __name__ == "__main__":
    test_0()
    test_207655800()
    test_207656499()
