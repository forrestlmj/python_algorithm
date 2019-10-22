# https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1131/
# 这道题比较绕，因为麻烦点在于如何判断是否欢乐数会进入到循环中
# 但是在题目描述中it loops endlessly in a cycle which does not include 1. 这一句已经提示了
# 如果当前运算结果出现过一次，那么则说明即将进入循环。因为下一步的运算肯定是之前遇到过的。


# 这道题说明 set可用作去重，同时他的结果也可以看做忽略时间的记录，很重要
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d_set = set()
        r = 0
        while n != 1:
            n = sum(int(i)**2 for i in str(n))
            if n not in d_set:
                d_set.add(n)
            else:
                return False
        return True

def test():
    s = Solution()
    assert s.isHappy(19) == True
    # assert s.isHappy([4,9,5],[9,4,9,8,4]) == 4

if __name__ == "__main__":
    test()