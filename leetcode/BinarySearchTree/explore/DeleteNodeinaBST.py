
import queue
class TreeNode:
    def __init__(self, x,l,r):
        self.val = x
        self.left = l
        self.right = r

class Solution:
    def deleteNode(self,root,key):
        if not root:
            return root
        if root.val == key:
            # 备份左右节点
            left, right = root.left, root.right
            if left:
                # 这段是最核心的部分，把左节点赋值给节点，然后
                p = left
                root = p
                while p.right:
                    p = p.right
                p.right = right
            else:
                root = right
            pass
        elif root.val > key:
            root.left = self.deleteNode(root.left,key)
        else:
            root.right = self.deleteNode(root.right,key)
        return root

s = Solution()
print(
s.deleteNode(
    TreeNode(5,
             TreeNode(3,
                        TreeNode(2,None,None),
                        TreeNode(4,None,None)
                      ),
             TreeNode(6,None,TreeNode(7,None,None)))
    ,3
))