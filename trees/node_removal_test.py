import unittest
from node import Node
from node_removal import remove, min_node

class TestNodeRemoval(unittest.TestCase):
  def setUp(self):
    self.tree = Node(15)
    self.tree.right = Node(20)
    self.tree.left = Node(10)

    self.tree.left.left = Node(8)
    self.tree.left.left.left = Node(2)

    self.tree.left.right = Node(11)
    self.tree.left.right.right = Node(12)

    self.tree.right.right = Node(30)
    self.tree.right.left = Node(18)
    self.tree.right.right.right = Node(35)
    self.tree.right.right.left = Node(25)

  def test_remove_leaf(self):
    self.tree = remove(self.tree, 25)
    self.assertTrue(self.tree.right.right.left == None)
    self.tree = remove(self.tree, 35)
    self.assertTrue(self.tree.right.right.right == None)

  def test_remove_node_with_left_child(self):
    self.tree = remove(self.tree, 8)
    self.assertTrue(self.tree.left.left.data == 2)

  def test_remove_node_with_right_child(self):
    self.tree = remove(self.tree, 11)
    self.assertTrue(self.tree.left.right.data == 12)

  def test_remove_node_with_both_children(self):
    self.tree = remove(self.tree, 30)
    self.assertTrue(self.tree.right.right.left.data == 25)
    self.assertTrue(self.tree.right.right.data == 35)


if __name__ == '__main__':
  unittest.main()