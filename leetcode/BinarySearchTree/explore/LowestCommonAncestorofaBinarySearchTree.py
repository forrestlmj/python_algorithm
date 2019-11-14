class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        def dfs(root,t):
            l = list()
            if root.val == t.val:
                l += [t]
            elif root.val > t.val:
                l = l + [root] +dfs(root.left,t)
            else:
                l = l+ [root] + dfs(root.right,t)
            return l
        p_p = dfs(root,p)
        # print(p_p)
        q_p = dfs(root,q)
        # print(q_p)
        c = None
        for i in range(min(len(p_p),len(q_p))):
            # print(p_p[i].val)
            # print(q_p[i].val)
            if p_p[i].val == q_p[i].val:
                c = p_p[i]
            else:
                break
        return c