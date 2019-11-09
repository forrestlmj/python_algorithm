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

class Solution(object):
    k = dict()
    # def init(x,y):
        # k[x],k[y] = None,None
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        # init(x,y)
        if not root:
            return False
        if root.val == x or root.val == y:
            return False
        x_papa,val,x_level = self.dfs(root,x,1)
        y_papa,val,y_level = self.dfs(root,y,1)
        # print("%s %d,%s %d" % (x_papa.val,x_level,y_papa.val,y_level))
        return x_papa.val != y_papa.val and y_level == x_level
    def dfs(self,cur,val,level):
        if not cur:
            return (None,None,None)
        if cur.left:
            if cur.left.val == val:
                return (cur,val,level)
            (c,v,l) = self.dfs(cur.left,val,level+1)
            if c:
                return (c,v,l)
        if cur.right:
            if cur.right.val == val:
                return (cur,val,level)
            (c,v,l) = self.dfs(cur.right,val,level+1)
            if c:
                return (c,v,l)
        return (None,None,None)

# str
def test():
    s = Solution()
    print(s.isCousins(TreeNode(1,
                         TreeNode(2,TreeNode(4,None,None),None),
                         TreeNode(3,None,None)),
                4,3))
if __name__ == "__main__":
    test()
