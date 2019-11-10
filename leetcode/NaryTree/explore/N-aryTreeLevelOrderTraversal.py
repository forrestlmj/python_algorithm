import queue


class Solution:
    def levelOrder(self, root):
        if not root:
            return None
        l, q = list(), queue.deque()
        q.append((root, 0))
        while q:
            cur, level = q.popleft()
            if level >= len(l):
                l.append([cur.val])
            else:
                l[level].append(cur.val)
            # l.append(cur.val)
            for c in cur.children:
                q.append((c, level + 1))

        return l
