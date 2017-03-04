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
        self.height = max([self.left_sub_height, self.right_sub_height])

    def update_bal_coeff(self):
        self.bal_coeff = self.right_sub_height - self.left_sub_height

    def __str__(self):
        return "data:{}\nheight:{}\nbal_coeff:{}\nleft_sub_tree_h:{}\nright_sub_tree_h:{}\n".format(self.data, self.height, self.bal_coeff, self.left_sub_height, self.right_sub_height)

def insert_to_avl(data, root):
    if not root:
        root = AVLNode(data)

    elif data < root.data:
        root.left = insert_to_avl(data, root.left)

        root.left_sub_height  = root.left.height + 1 # Only this changes
        root.update_height()
        root.update_bal_coeff()
        print(root)

    elif data >= root.data:
        root.right = insert_to_avl(data, root.right)

        root.right_sub_height  = root.right.height  + 1 # Only this changes
        root.update_height()
        root.update_bal_coeff()
        print(root)

    return root

def in_order_traversal(root):
    if root.left:
        in_order_traversal(root.left)
    print("data:{}, h:{}, bal_coeff:{}".format(root.data, root.height, root.bal_coeff))
    if root.right:
        in_order_traversal(root.right)

if __name__ == '__main__':
    root = AVLNode(10)
    for num in [5, 12, 15, 16]:
        insert_to_avl(num, root)

    # add_balance_coeff(root)
    # in_order_traversal(root)
