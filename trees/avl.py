from node import Node

class AVLNode(Node):
    def __init__(self, *args):
        super().__init__(*args)
        self.bal_coeff = None

class AVLTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.rec_insert(data, self.root)

    def rec_insert(self, data, root):
        if not root:
            root = AVLNode(data)
            root.left = None
            root.right = None
        elif data < root.data:
            root.left = self.rec_insert(data, root.left)
        elif data >= root.data:
            root.right = self.rec_insert(data, root.right)
        return root

    def in_order(self, callback):
        result = []
        for node in self.rec_in_order(self.root):
            result.append(callback(node))
        return result

    def rec_in_order(self, root):
        if root.left:
            yield from self.rec_in_order(root.left)
        yield root
        if root.right:
            yield from self.rec_in_order(root.right)

    def height(self, node):
        left_height = 0
        right_height = 0

        if node.left:
            left_height = 1 + self.height(node.left)

        if node.right:
            right_height = 1 + self.height(node.right)

        return max(left_height, right_height)

    def recalculate_balances(self, node):
        left_height = 0
        right_height = 0

        if node.left:
            left_height = 1 + self.recalculate_balances(node.left)

        if node.right:
            right_height = 1 + self.recalculate_balances(node.right)

        node.bal_coeff = left_height - right_height
        return max(left_height, right_height)