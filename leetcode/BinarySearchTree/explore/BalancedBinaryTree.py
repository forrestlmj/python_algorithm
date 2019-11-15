import queue


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def not_balanced(s):
            if len(s) > 2:
                return True
            elif len(s) == 2:
                (a, b) = s
                if abs(a - b) > 1:
                    return True
            return False

        q = queue.deque()
        if not root:
            return True
        level_set = set()
        q.append((root, 0))
        while q:
            (node, level) = q.popleft()
            if not node.left and not node.right:
                # print(level)
                level_set.add(level)
                if not_balanced(level_set):
                    return False
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return True