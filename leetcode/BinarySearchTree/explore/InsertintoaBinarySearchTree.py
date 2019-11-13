# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self,x, l,r):
#         self.val = x
#         self.left = l
#         self.right = r
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        d_y = root
        self.dfs(root,val)
        return d_y
    def dfs(self,cur,val):
        if val < cur.val:
            if not cur.left:
                cur.left = TreeNode(val)
            else:
                self.dfs(cur.left,val)
        else:
            if not cur.right:
                cur.right = TreeNode(val)
            else:
                self.dfs(cur.right,val)
        return cur
def test():
    s = Solution()
    root = TreeNode(4,
                    TreeNode(2,TreeNode(1),TreeNode(3)),
                    TreeNode(7))
    s.insertIntoBST(root,5)
if __name__ == "__main__":
    test()