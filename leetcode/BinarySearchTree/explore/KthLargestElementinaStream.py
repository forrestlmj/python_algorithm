class KthLargest:
    class node():
        def __init__(self, val, cnt):
            self.val = val
            self.right = None
            self.left = None
            self.cnt = cnt

    def __init__(self, k: int, nums):
        if nums:
            self.root = self.node(nums[0], 0)
            for i in nums[1:]:
                self.root = self.insert(self.root, i)
        else:
            self.root = None
        self.k = k - 1

    def add(self, val: int) -> int:
        self.root = self.insert(self.root, val)
        return self.findKthLargest(self.root, self.k)

    def insert(self, root, key):
        if not root:
            return self.node(key, 0)

        elif root.val > key:
            root.left = self.insert(root.left, key)
        else:
            root.cnt += 1
            root.right = self.insert(root.right, key)

        return root

    def findKthLargest(self, root, k):
        if not root:
            return -1

        elif root.cnt == k:
            return root.val

        elif root.cnt > k:
            return self.findKthLargest(root.right, k)
        else:
            return self.findKthLargest(root.left, k - root.cnt - 1)

k = 3
arr = [4,5,8,2]
kthLargest =  KthLargest(3, arr)
print(kthLargest.add(3))   # returns 4
print(kthLargest.add(5)  ) # returns 5
print(kthLargest.add(10) ) # returns 5
print(kthLargest.add(9)  ) # returns 8
print(kthLargest.add(4)  ) # returns 8