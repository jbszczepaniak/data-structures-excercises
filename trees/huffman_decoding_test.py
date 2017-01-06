import unittest
from huffman_decoding import HuffNode

class TestTopView(unittest.TestCase):
    def test_node_has_frequency_and_data(self):
        node = HuffNode(data=2, freq=1)
        self.assertEqual(node.data ,2)
        self.assertEqual(node.freq ,1)

if __name__ == '__main__':
    unittest.main()
