from random import randint, seed

seed(11111)

class AVLNode():
    def __init__(self, data):
        self.bal_coeff = 0
        self.data = data
        self.height = 0
        self.right = None
        self.left = None

    def update_height(self):
        self.height = height(self) - 1 # -1 is an adjustment

    def update_bal_coeff(self):
        self.bal_coeff = height(self.right) - height(self.left)

    def __str__(self):
        return "data:{}\nheight:{}\nbal_coeff:{}\n".format(self.data, self.height, self.bal_coeff)

def insert_to_avl(data, root):
    if not root:
        root = AVLNode(data)

    elif data < root.data:
        root.left = insert_to_avl(data, root.left)

        root.update_height()
        root.update_bal_coeff()

        if abs(root.bal_coeff) > 1:

            root = rotate(root)

        # print(root)

    elif data >= root.data:
        # print(data)
        root.right = insert_to_avl(data, root.right)

        root.update_height()
        root.update_bal_coeff()

        if abs(root.bal_coeff) > 1:
            root = rotate(root)

    return root

def height(root):
    if not root:
        return 0
    return (max(1 + height(root.left), 1 + height(root.right)))

def rotate(root):
    if root.bal_coeff > 0:
        if root.right.bal_coeff >= 0:
            return rotate_single_left(root)
        else:
            return rotate_right_left(root)
    elif root.bal_coeff < 0:
        if root.left.bal_coeff < 0:
            return rotate_single_right(root)
        else:
            return rotate_left_right(root)

def rotate_single_left(root):
    new_root = root.right
    temp = new_root.left
    new_root.left = root
    root.right = temp

    root.update_height()
    root.update_bal_coeff()
    new_root.update_height()
    new_root.update_bal_coeff()

    return new_root


def rotate_right_left(root):
    root.right = rotate_single_right(root.right)
    return rotate_single_left(root)

def rotate_single_right(root):
    new_root = root.left
    temp = new_root.right
    new_root.right = root
    root.left = temp

    root.update_height()
    root.update_bal_coeff()
    new_root.update_height()
    new_root.update_bal_coeff()

    return new_root


def rotate_left_right(root):
    root.left = rotate_single_left(root.left)
    return rotate_single_right(root)

def in_order_traversal(root):
    if root.left:
        in_order_traversal(root.left)
    print("data:{}, h:{}, bal_coeff:{}".format(root.data, root.height, root.bal_coeff))
    if root.right:
        in_order_traversal(root.right)

if __name__ == '__main__':
    root = AVLNode(10)
    for num in [5, 12, 15, 16, 17, 18 , 4, 3 ]:
        root = insert_to_avl(num, root)

    in_order_traversal(root)
    # print(root.left.left.left)