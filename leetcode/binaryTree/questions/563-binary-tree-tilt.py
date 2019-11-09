# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x,left,right):
        self.val = x
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    s = 0
    def findTilt(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.s
    def dfs(self , cur):
        if not cur:
            return 0
        left,right = self.dfs(cur.left), self.dfs(cur.right)
        self.s += abs(left-right)
        return cur.val+left+right


# str
def test():
    s = Solution()
    print(
        s.findTilt(
            TreeNode(1,TreeNode(2,None,None),TreeNode(1,None,None))
        )
    )
    print(s.findTilt(
        TreeNode(1,
                 TreeNode(1,
                          TreeNode(1,None,None),
                          TreeNode(1,None,None)
                          ),
                 TreeNode(1,
                          None,
                          TreeNode(1,None,None)
                          )
                 )
    ))
if __name__ == "__main__":
    test()