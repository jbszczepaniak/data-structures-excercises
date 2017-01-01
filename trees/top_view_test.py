import unittest
from node import Node
from top_view import top_view

class TestTopView(unittest.TestCase):
    def setUp(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.right.left = Node(6)
        self.root.right.right = Node(7)
        self.root.right.left.right = Node(8)
        self.root.right.right.right = Node(9)
        self.root.right.right.left = Node(10)
        self.root.right.right.left.left = Node(11)
        self.root.right.right.left.left.right = Node(12)
        self.root.right.right.left.left.right.right = Node(13)
        self.root.right.right.left.left.right.right.right = Node(14)
        self.root.right.right.left.left.right.right.right.right = Node(15)
        self.root.right.right.left.left.right.right.right.right.left = Node(16)
        self.root.right.right.left.left.left = Node(17)
        self.root.right.right.left.left.left.left = Node(18)
        self.root.right.right.left.left.left.left.left = Node(19)
        self.root.right.right.left.left.left.left.left.left = Node(20)
        self.root.right.right.left.left.left.left.left.left.left = Node(21)
        self.root.right.right.left.left.left.left.left.left.left.left = Node(22)
        self.root.right.right.left.left.left.left.left.left.left.left.left = Node(23)


    def test_(self):
        top_view_nodes = top_view(self.root)
        top_view_nodes_values = [ v[0] for k,v in sorted(top_view_nodes.items())]
        self.assertEqual([23, 22, 21, 20, 19, 4, 2, 1, 3, 7, 9, 15] , top_view_nodes_values)

if __name__ == '__main__':
    unittest.main()