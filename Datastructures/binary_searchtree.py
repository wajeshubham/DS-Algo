class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert_element(self, data):
        if data < self.data:
            if self.left:
                return self.left.insert_element(data)
            else:
                self.left = BinarySearchTree(data)
                return

        if data > self.data:
            if self.right:
                return self.right.insert_element(data)
            else:
                self.right = BinarySearchTree(data)
                return

    def is_exist(self, data):
        if self.data == data:
            return True
        if data < self.data:
            if self.left:
                return self.left.is_exist(data)
        if data > self.data:
            if self.right:
                return self.right.is_exist(data)
        return False

    def find_max(self):
        if self.right is not None:
            return self.right.find_max()
        return self.data

    def find_min(self):
        if self.left is not None:
            return self.left.find_min()
        return self.data

    def inorder_traversal(self):
        tree = []  # left sub tree --> node --> right sub tree
        if self.left:
            tree += self.left.inorder_traversal()

        tree.append(self.data)

        if self.right:
            tree += self.right.inorder_traversal()
        return tree

    def preorder_traversal(self):
        tree = [self.data]  # node --> left sub tree --> right sub tree
        if self.left:
            tree += self.left.preorder_traversal()

        if self.right:
            tree += self.right.preorder_traversal()
        return tree

    def postorder_traversal(self):
        tree = []  # left sub tree --> right sub tree --> node
        if self.left:
            tree += self.left.postorder_traversal()

        if self.right:
            tree += self.right.postorder_traversal()

        tree.append(self.data)
        return tree

    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if self.right is None and self.left is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)
        return self

