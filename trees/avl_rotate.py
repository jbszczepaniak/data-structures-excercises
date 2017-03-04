from random import randint, seed

seed(11111)

class AVLNode():
    def __init__(self, data):
        self.bal_coeff = 0
        self.data = data
        self.height = 0
        self.right_sub_height = 0
        self.left_sub_height = 0
        self.right = None
        self.left = None

    def update_height(self):
        root.height = max([root.left_sub_height, root.right_sub_height])

    def update_bal_coeff(self):
        root.bal_coeff = root.right_sub_height - root.left_sub_height

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

    elif data < root.data:
        root.left = insert_to_avl(data, root.left)

        root.left_sub_height  = root.left.height + 1 # Only this changes

        root.update_height()
        root.update_bal_coeff()

        print("data:{}, h:{}, bal_coeff:{}".format(root.data, root.height, root.bal_coeff))
    elif data >= root.data:
        root.right = insert_to_avl(data, root.right)

        root.right_sub_height  = root.right.height  + 1# Only this changes

        root.update_height()
        root.update_bal_coeff()
        print("data:{}, h:{}, bal_coeff:{}".format(root.data, root.height, root.bal_coeff))
    return root

def in_order_traversal(root):
    if root.left:
        in_order_traversal(root.left)
    print("data:{}, h:{}, bal_coeff:{}".format(root.data, root.height, root.bal_coeff))
    if root.right:
        in_order_traversal(root.right)

if __name__ == '__main__':
    root = AVLNode(10)
    for num in [5, 12, 15, 11]:
        insert_to_avl(num, root)

    # add_balance_coeff(root)
    # in_order_traversal(root)
