class BinaryTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self._size = 0

    def is_empty(self):
        return self.root is None

    def insert(self, value):
        if not self.root:
            self.root = BinaryTree.Node(value)
            self._size = 1
            return
        cur = self.root
        while True:
            if value < cur.data:
                if not cur.left:
                    cur.left = BinaryTree.Node(value)
                    break
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = BinaryTree.Node(value)
                    break
                cur = cur.right
        self._size += 1

    def search(self, value):
        cur = self.root
        while cur:
            if value == cur.data:
                return True
            cur = cur.left if value < cur.data else cur.right
        return False

    def traverse_inorder(self):
        result = []
        def _inorder(node):
            if not node:
                return
            _inorder(node.left)
            result.append(node.data)
            _inorder(node.right)
        _inorder(self.root)
        return result

    def traverse_preorder(self):
        result = []
        def _preorder(node):
            if not node:
                return
            result.append(node.data)
            _preorder(node.left)
            _preorder(node.right)
        _preorder(self.root)
        return result

    def traverse_postorder(self):
        result = []
        def _postorder(node):
            if not node:
                return
            _postorder(node.left)
            _postorder(node.right)
            result.append(node.data)
        _postorder(self.root)
        return result

    def _min_value_node(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current

    def delete(self, value):
        self.root, deleted = self._delete_recursive(self.root, value)
        if deleted:
            self._size -= 1

    def _delete_recursive(self, root, value):
        if not root:
            return root, False

        deleted = False
        if value < root.data:
            root.left, deleted = self._delete_recursive(root.left, value)
        elif value > root.data:
            root.right, deleted = self._delete_recursive(root.right, value)
        else:
            if not root.left:
                return root.right, True
            elif not root.right:
                return root.left, True

            temp = self._min_value_node(root.right)
            root.data = temp.data
            root.right, _ = self._delete_recursive(root.right, temp.data)
            deleted = True

        return root, deleted

    def __len__(self):
        return self._size

    def __repr__(self):
        return f"BinaryTree(in={self.traverse_inorder()})"



# В этом дереве каждый элемент хранится в узле Node:
# - у узла есть значение (data), ссылка влево (left) и вправо (right)

# insert(value):
# добавляет значение в дерево — идёт от корня и вставляет в нужное место

# search(value):
# ищет значение в дереве — возвращает True, если найдено, иначе False

# traverse_inorder():
# обходит дерево по порядку (лево - узел - право) и возвращает отсортированный список

# __len__():
# возвращает количество элементов в дереве, работает с len(tree)

# __repr__():
# возвращает строку с отсортированными значениями, удобно для print(tree)
