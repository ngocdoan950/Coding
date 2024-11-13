from tree_node import TreeNode

class BinarySearchTree:
    """
    For each node, all values in it's subtree is smaller than its value

    + Operators:
        - search:
            - các note bên phải sẽ lớn hơn & bên trái sẽ nhỏ hơn so với gôc.
        - insert
        - delete
        - update
    """
    def __init__(self) -> None:
        pass
    

    def preOrder(self, node: TreeNode):
        print(node.value)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def postOrder(self, node: TreeNode):
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.value)

    def inOrder(self, node: TreeNode):
        self.inOrder(node.left)
        print(node.value)
        self.inOrder(node.right)