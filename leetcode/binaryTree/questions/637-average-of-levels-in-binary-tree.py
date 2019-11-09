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
import queue
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return None
        l = list()
        q = queue.deque()
        q.append((root,0))
        while len(q) > 0:
            cur,level = q.popleft()
            if level == len(l):
                l.append([cur.val])
            else:
                l[level].append(cur.val)
            if cur.left:
                q.append((cur.left,level+1))
            if cur.right:
                q.append((cur.right,level+1))
        return [sum(level)/len(level) for level in l]
def test():
    s = Solution()
    print(s.averageOfLevels(
        TreeNode(3,
                 TreeNode(9,None,None),
                 TreeNode(20,
                          TreeNode(15,None,None),
                          TreeNode(7,None,None)
                          )
                 )
    ))
if __name__ == "__main__":
    test()