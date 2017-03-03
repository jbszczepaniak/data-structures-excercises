import unittest
from node import Node
from node_removal import remove

class TestNodeRemoval(unittest.TestCase):
  def setUp(self):
    self.tree = Node(15)
    self.tree.right = Node(20)
    self.tree.left = Node(10)
    self.tree.right.right = Node(30)
    self.tree.right.left = Node(18)
    self.tree.right.right.right = Node(35)
    self.tree.right.right.left = Node(25)

  def test_remove_leaf(self):
    self.tree = remove(self.tree, 25)
    # print(self.tree.data)
    self.assertTrue(self.tree.right.right.left == None)

if __name__ == '__main__':
  unittest.main()