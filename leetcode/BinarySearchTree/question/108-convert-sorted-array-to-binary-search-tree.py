# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def dfs(l):
            if not l:
                return None
            val = l[int(len(l)/2)]
            print(val)
            root = TreeNode(val)            
            root.left = dfs(l[:int(len(l)/2)])
            root.right = dfs(l[int(len(l)/2)+1:])
            return root
        return dfs(nums)

s = Solution()
c = s.sortedArrayToBST([-10,-3,0,5,9])
print(c)
d = s.sortedArrayToBST([-10])
