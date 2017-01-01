import unittest
from node import Node
from level_traversal import level_traversal

class TestLevelTraversal(unittest.TestCase):
    def setUp(self):
        self.simple_balanced = Node(1)
        self.simple_balanced.left = Node(2)
        self.simple_balanced.right = Node(3)
        self.simple_balanced.left.left = Node(4)
        self.simple_balanced.left.right = Node(5)
        self.simple_balanced.right.left = Node(6)
        self.simple_balanced.right.right = Node(7)

        self.unbalanced_tree = Node(1)
        self.unbalanced_tree.left = Node(2)
        self.unbalanced_tree.left.left = Node(6)
        self.unbalanced_tree.left.left.right = Node(7)
        self.unbalanced_tree.right = Node(3)
        self.unbalanced_tree.right.left = Node(4)
        self.unbalanced_tree.right.right = Node(5)
        self.unbalanced_tree.right.right.right = Node(8)
        self.unbalanced_tree.right.right.right.left = Node(9)

    def test_simple_balanced_traversal(self):
        traversed = level_traversal(self.simple_balanced)
        self.assertEqual([1,2,3,4,5,6,7], traversed)

    def test_unbalanced_tree_traversal(self):
        traversed = level_traversal(self.unbalanced_tree)
        self.assertEqual([1,2,3,6,4,5,7,8,9], traversed)

if __name__ == '__main__':
    unittest.main()