from random import randint, seed

seed(11111)

class AVLNode():
    def __init__(self, data):
        self.bal_coeff = None
        self.data = data
        self.height = None
        self.right = None
        self.left = None


def height(root):
    if not root:
        return 0
    return (max(1 + height(root.left), 1 + height(root.right)))

def add_balance_coeff(root):
    if not root:
        return 0
    left_height = 1 + add_balance_coeff(root.left)
    right_height = 1 + add_balance_coeff(root.right)

    print(left_height - right_height)
    return (max(left_height, right_height))


def insert_to_avl(data, root):
    if not root:
        root = AVLNode(data)
        root.left = None
        root.right = None
    elif data < root.data:
        root.left = insert_to_avl(data, root.left)
    elif data >= root.data:
        root.right = insert_to_avl(data, root.right)
    return root

def in_order_traversal(root):
    if root.left:
        in_order_traversal(root.left)
    print(root.data, end=" ")
    if root.right:
        in_order_traversal(root.right)

if __name__ == '__main__':
    root = AVLNode(10)
    for num in [5,2,8,1,3,7,9]:
        insert_to_avl(num, root)

    add_balance_coeff(root)
    in_order_traversal(root)