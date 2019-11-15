class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def findMode(self, root: TreeNode) -> [int]:
        def dfs(cur):
            if not cur:
                return
            if cur.val not in d:
                d[cur.val] = 1
            else:
                d[cur.val] += 1
            dfs(cur.left)
            dfs(cur.right)
        d = dict()
        dfs(root)
        max = 0
        re = list()
        for (k,v) in d.items():
            if v > max:
                re.clear()
                re.append(k)
                max = v
            elif v == max:
                re.append(k)
        return re