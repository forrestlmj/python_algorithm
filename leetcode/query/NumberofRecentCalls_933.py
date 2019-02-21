# https://leetcode.com/problems/number-of-recent-calls/
class RecentCounter:

    def __init__(self):
        self.time = 3000
        self.queue = list()

    def ping(self, t: 'int') -> 'int':
        if len(self.queue) == 0:
            self.queue.append(t)
        else:
            while len(self.queue) >0 and t - self.queue[0] > 3000:
                self.queue.remove(self.queue[0])
            self.queue.append(t)
        return len(self.queue)
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

def test_0():
    # 1 <= t <= 1000
    c = RecentCounter()
    assert c.ping(1) == 1
    assert c.ping(100) == 2
    assert c.ping(3001) == 3
    assert c.ping(3002) == 3
    assert c.ping(10000) == 1
if __name__ == "__main__":
    test_0()
