import unittest
from huffman_decoding import HuffNode, decode

class TestHuffmanDecoding(unittest.TestCase):
    def setUp(self):
        self.tree = HuffNode(data=0, freq=5)
        self.tree.left = HuffNode(data=0, freq=2)
        self.tree.right  = HuffNode(data='A', freq=3)
        self.tree.left.left = HuffNode(data='B', freq=1)
        self.tree.left.right = HuffNode(data='C', freq=1)

    def test_one_character_input_stream(self):
        stream = '1'
        word = decode(stream, self.tree)
        self.assertEqual(word, 'A')

    def test_repeating_symbol(self):
        stream = '111'
        word = decode(stream, self.tree)
        self.assertEqual(word, 'AAA')

    def test_hackerrank_input(self):
        word = decode('1001011', self.tree)
        self.assertEqual(word,'ABACA')

if __name__ == '__main__':
    unittest.main()
