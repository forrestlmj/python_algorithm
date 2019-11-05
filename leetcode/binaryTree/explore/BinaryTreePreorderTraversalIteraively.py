class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack,re = [root],list()
        while len(stack)>0:
            node = stack.pop()
            if node:
                re.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return re