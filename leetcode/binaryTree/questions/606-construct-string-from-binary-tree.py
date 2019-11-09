# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x,left,right):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        # d_t = TreeNode(None)
        if not t:
            return ""
        return self.dfs(t)
        # print(path)
    def dfs(self,cur):
        if not cur.left and not cur.right:
            return str(cur.val)
        l = str(cur.val)
        left = (self.dfs(cur.left) if cur.left else "")
        # l = l + (("(" + left +")") if left else "")
        l = l + "(" + left +")"

        right = (self.dfs(cur.right) if cur.right else "" )
        l = l + (("(" + right + ")") if right else "")
        # l = l + "(" + right + ")"
        return l


def test():
    s = Solution()
    t = TreeNode(
        1,
        TreeNode(2,TreeNode(4,None,None),None),
        TreeNode(3,None,None)
    )
    print(s.tree2str(t))
    s = Solution()
    t = TreeNode(
        1,
        TreeNode(2,None,TreeNode(4,None,None)),
        TreeNode(3,None,None)
    )
    print(s.tree2str(t))
if __name__ == "__main__":
    test()