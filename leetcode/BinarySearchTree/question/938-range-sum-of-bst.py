class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        """
        直接提交
        :param root:
        :param L:
        :param R:
        :return:
        """
        l = list()
        def dfs(root: TreeNode, L: int, R: int):
            if not root:
                return
            if root.left:
                dfs(root.left,L,R)
            if root.val >= L and root.val <= R:
                l.append(root.val)
            if root.right:
                dfs(root.right,L,R)
        dfs(root,L,R)
        print(l)
        return sum(l)
