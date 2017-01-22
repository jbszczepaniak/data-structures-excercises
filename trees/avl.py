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

    def in_order(self):
        result = []
        for value in self.rec_in_order(self.root):
            result.append(value)
        return result

    def rec_in_order(self, root):
        if root.left:
            yield from self.rec_in_order(root.left)
        yield root.data
        if root.right:
            yield from self.rec_in_order(root.right)