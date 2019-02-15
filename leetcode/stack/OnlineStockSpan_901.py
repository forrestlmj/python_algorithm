# https://leetcode.com/problems/online-stock-span/
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


class StockSpanner(object):
    def __init__(self):
        self.stack = Stack()
        # 栈结构：参数零为价格，参数1为绝对天数，相减为相对天数
        self.stack.push([float("inf"), 0])
        # 每调用一次next,time+1
        self.time = 0

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.time += 1
        if price < self.stack.top()[0]:
            self.stack.push([price, self.time])
            return 1
        else:

            while price >= self.stack.top()[0]:
                self.stack.pop()
            last_date = self.stack.top()[1]
            self.stack.push([price, self.time])
            return self.time-last_date
            #     self.stack.push([price, current[1]+1])
            # else:
            #     self.stack.push([print(), 1])


        # Your StockSpanner object will be instantiated and called as such:
        # obj = StockSpanner()
        # param_1 = obj.next(price)
def test_0():
    q = [[],[100],[80],[60],[70],[60],[75],[85]]
    obj = StockSpanner()
    assert obj.next(100) == 1
    assert obj.next(80) == 1
    assert obj.next(60) == 1
    assert obj.next(70) == 2
    assert obj.next(60) == 1
    assert obj.next(75) == 4
    assert obj.next(85) == 6
    assert obj.next(85) == 7
    assert obj.next(60) == 1

if __name__ == "__main__":
    test_0()