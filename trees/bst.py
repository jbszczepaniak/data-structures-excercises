from node import Node
class BST():
    def __init__(self):
        self.root = None

def insert(data, root):
    if not root:
        root = Node(data)
        root.right = None
        root.left = None
    elif data < root.data:
        root.left = insert(data, root.left)
    elif data > root.data:
        root.right = insert(data, root.right)
    return root

def remove(data, root):
    if data < root.data:
        root.left = remove(data, root.left)
    elif data > root.data:
        root.right = remove(data, root.right)
    else:
        if (not root.left) and (not root.right):
            return None

        if (root.left) and (not root.right):
            return root.left

        if (not root.left) and (root.right):
            return root.right

        else:
            right_sub_tree_min = bst_min_node(root.right)
            temp_data = right_sub_tree_min.data
            root = remove(temp_data, root)
            root.data = temp_data

    return root

def bst_min_node(root):
    if not root:
        return
    if root.left:
        return bst_min_node(root.left)
    else:
        return root

def in_order_print(root):
    if not root:
        return
    if root.left:
        in_order_print(root.left)
    print(root.data)
    if root.right:
        in_order_print(root.right)

previous = -999999999
def check_binary_search_tree_(root):
    '''
    my working solution!
    '''
    global previous

    if root:
        if not check_binary_search_tree_(root.left) :
            return False

        if root.data <= previous :
            return False
        previous = root.data

        if not check_binary_search_tree_(root.right):
            return False

    return True


if __name__ == '__main__':
    bst1 = Node(16)
    bst1.left = Node(4)
    bst1.right = Node(20)
    bst1.left.left = Node(3)
    bst1.left.right = Node(10)
    bst1.right.right = Node(25)
    bst1.left.left.left = Node(1) # tu było jeden
    bst1.left.right.left = Node(8)
    bst1.right.right.left = Node(1)
    bst1.left.left.left.right = Node(2)
    bst1.left.right.left.left = Node(7)
    bst1.left.right.left.right = Node(9)
    bst1.left.right.left.left.left = Node(5)
    bst1.left.right.left.left.left.right = Node(6)

    in_order_print(bst1)
    print(check_binary_search_tree_(bst1))