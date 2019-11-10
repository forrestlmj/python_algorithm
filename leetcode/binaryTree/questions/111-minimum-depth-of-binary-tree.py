# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x,left,right):
        self.val = x
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = queue.deque()
        l = list()
        level = 0
        q.append((root,1))
        while len(q)>0:
            (cur,level) = q.popleft()
            if not cur.left and not cur.right:
                return level
            if cur.left:
                q.append((cur.left,level+1))
            if cur.right:
                q.append((cur.right,level+1))

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