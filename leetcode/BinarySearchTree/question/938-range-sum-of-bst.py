class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    a = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        """
        使用二叉树的特性，左面子树的值小于右边子树的值，
        :param root:
        :param L:
        :param R:
        :return:
        """

        def dfs(cur, l, r):
            if not cur:
                return None
            if cur.val >= l and cur.val <= r:
                self.a += cur.val
            if l < cur.val:
                dfs(cur.left, l, r)
            if r > cur.val:
                dfs(cur.right, l, r)

        dfs(root, L, R)
        return self.a