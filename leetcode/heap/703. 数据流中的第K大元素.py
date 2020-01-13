# -*- coding: utf-8 -*- 
# @Time : 2020/1/13 下午9:52 
# @Author : yangchengkai
# @File : 703. 数据流中的第K大元素.py
import heapq
class KthLargest:
    # TODO 超出时间，提示：这里不能直接heapify
    nums = list()
    k = -1
    def __init__(self, k: int, nums):
        self.nums = nums
        heapq.heapify(nums)
        self.k = k
    def add(self, val: int) -> int:

        heapq.heappush(self.nums,val)
        t = heapq.nlargest(self.k,self.nums)[-1]

        return t


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/kth-largest-element-in-a-stream
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
