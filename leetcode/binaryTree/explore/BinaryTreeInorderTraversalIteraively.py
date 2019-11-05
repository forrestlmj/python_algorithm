class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack,re = [root],list()
        while len(stack)>0:
            node = stack.pop()
            if node:
                stack.append(node.right)
                re.append(node.val)
                stack.append(node.left)
        return re