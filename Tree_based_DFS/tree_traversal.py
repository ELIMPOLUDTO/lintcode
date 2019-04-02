'树的遍历'
__author__ = 'ChenKX'

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    #先序遍历：根节点，左子树，右子树
    #递归实现
    def preorderTraversal(self, root):
        self.results = []
        self.traverse(root)
        return self.results
        
    def traverse(self, root):
        if root is None:
            return
        self.results.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)
    #先序遍历的非递归实现
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder

    #中序遍历：in_order:左子树，根节点，右子树
    #递归实现
    def inorderTraversal(self, root):
        self.results = []
        self.inorder_traverse(root)
        return self.results
    def inorder_traverse(self, root):
        if root is None:
            return
        self.inorder_traverse(root.left)
        self.results.append(root.val)
        self.inorder_traverse(root.right)
    #非递归实现
    def inorderTraversal(self, root):
        # write your code here
        self.result = self.traversal(root)
        return self.result
        
    def traversal(self, root):
        if root is None:
            return []
        
        dummy_node = TreeNode(0)
        dummy_node.right = root
        #######
        stack = [dummy_node]
        inroder= []
        
        while(stack):
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                inroder.append(stack[-1].val)
        return inroder
    #后序遍历
    def postorderTraversal(self, root):
        self.res = []
        self.traversal(root)
        return self.res       
    def traversal(self,root):
        if root is None:
            return
        self.traversal(root.left)
        self.traversal(root.right)
        self.res.append(root.val)
    #后序遍历非递归实现
    def postorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        postorder = []
        while stack:
            node = stack.pop()
            postorder.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        res = []
        while postorder:
            res.append(postorder.pop())
        return res