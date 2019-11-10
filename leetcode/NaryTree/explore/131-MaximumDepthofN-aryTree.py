
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children



class Solution:
    def __init__(self):
        self.maxl = 0
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        return self.dfs(root)
    def dfs(self,cur):
        if not cur:
            return 0
        maxl = 0
        for c in cur.children:
            cur_l = self.dfs(c)
            maxl = max(maxl, cur_l)
        return maxl+1
s = Solution()

print(s.maxDepth(
    Node(1,
         [
             Node(2,[Node(5,[]), Node(6,[])]),
             Node(3,[]),
             Node(4,[])
         ])
))
s = Solution()

print(s.maxDepth(
    Node(1,
         [
             Node(2,[Node(3,[]), Node(4,[])]),
             Node(5,[Node(6,[])])
         ])
))