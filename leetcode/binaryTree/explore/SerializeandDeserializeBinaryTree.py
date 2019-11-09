# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x,left,right):
        self.val = x
        self.left = left
        self.right = right
import queue
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        l = list()
        q = queue.deque()
        if not root:
            return l
        q.append(root)
        # l.append(root.val)
        while len(q) > 0:
            cur = q.popleft()
            # l.append(cur.val)
            if cur:
                l.append(cur.val)
                q.append(cur.left)
                q.append(cur.right)
            else:
                l.append("#")
        a = "".join((str(i) if isinstance(i,int) else "#" for i in l))
        print(a)
        return a
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
s = Codec()
s.serialize(
    TreeNode(3,
       TreeNode(5,
            TreeNode(6,None,None),
            TreeNode(2,TreeNode(7,None,None),TreeNode(4,None,None))
            ),
        TreeNode(1,
             TreeNode(0,None,None),
             TreeNode(8, None, None),
             ),
       )
)
s.serialize(
    TreeNode(3,
       TreeNode(5,
            TreeNode(6,None,None),
            TreeNode(2,TreeNode(7,None,None),TreeNode(4,None,None))
            ),
        TreeNode(1,
             TreeNode(0,None,None),
             TreeNode(8, None, None),
             ),
       )
)
a = 1
# s.deserialize("35162 8  74        ")