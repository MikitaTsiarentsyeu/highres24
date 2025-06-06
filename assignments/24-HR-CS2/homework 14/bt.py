from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return

        queue = deque([self.root])
        while queue:
            current = queue.popleft()

            if current.left is None:
                current.left = TreeNode(value)
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = TreeNode(value)
                return
            else:
                queue.append(current.right)

    def search(self, value):
        if self.root is None:
            return None

        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if current.value == value:
                return current
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return None

    def delete(self, value):
        if self.root is None:
            return

        queue = deque([self.root])
        node_to_delete = None
        last_node = None
        parent_of_last = None

        while queue:
            current = queue.popleft()

            if current.value == value:
                node_to_delete = current

            if current.left:
                parent_of_last = current
                queue.append(current.left)

            if current.right:
                parent_of_last = current
                queue.append(current.right)

            last_node = current

        if node_to_delete is not None:
            node_to_delete.value = last_node.value

            if parent_of_last.left == last_node:
                parent_of_last.left = None
            elif parent_of_last.right == last_node:
                parent_of_last.right = None

    def traverse_inorder(self):
        result = []

        def in_order(node):
            if node:
                in_order(node.left)
                result.append(node.value)
                in_order(node.right)

        in_order(self.root)
        return result

    def traverse_preorder(self):
        result = []

        def pre_order(node):
            if node:
                result.append(node.value)
                pre_order(node.left)
                pre_order(node.right)

        pre_order(self.root)
        return result

    def traverse_postorder(self):
        result = []

        def post_order(node):
            if node:
                post_order(node.left)
                post_order(node.right)
                result.append(node.value)

        post_order(self.root)
        return result



tree = BinaryTree()
for val in [10, 5, 15, 3, 7, 12, 18]:
    tree.insert(val)

print("Inorder:", tree.traverse_inorder())
print("Preorder:", tree.traverse_preorder())
print("Postorder:", tree.traverse_postorder())

found = tree.search(7)
print("Search 7:", found.value if found else "Not found")

tree.delete(15)
print("After deleting 15 (inorder):", tree.traverse_inorder())