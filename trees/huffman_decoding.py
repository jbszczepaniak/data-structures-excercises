import io
class HuffNode():
    def __init__(self, data, freq):
        self.data = data
        self.freq = freq
        self.right = None
        self.left = None

def decode(stream, root_tree):
    result = []
    curr_node = root_tree

    for char in stream:
        if char == '0':
            curr_node = curr_node.left
        if char == '1' :
            curr_node = curr_node.right
        if not curr_node.left and not curr_node.right:
            result.append(curr_node.data)
            curr_node = root_tree
    return "".join(result)