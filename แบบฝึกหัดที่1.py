class Node:
    def __init__(self, value):
        self.value = value  # ค่าของ Node
        self.left = None  # ตัวชี้ไปยังลูกซ้าย
        self.right = None  # ตัวชี้ไปยังลูกขวา

class BinaryTree:
    def __init__(self):
        self.root = None  # เริ่มต้นไม่มีต้นไม้

    # ฟังก์ชันเพื่อเพิ่ม node ใหม่
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    # ฟังก์ชันช่วยเพื่อหาตำแหน่งที่เหมาะสมในการเพิ่ม node
    def _insert(self, root, new_node):
        if new_node.value < root.value:
            if root.left is None:
                root.left = new_node
            else:
                self._insert(root.left, new_node)
        else:
            if root.right is None:
                root.right = new_node
            else:
                self._insert(root.right, new_node)

    # ฟังก์ชัน inorder traversal
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)

    # ฟังก์ชัน preorder traversal
    def preorder(self, root):
        if root:
            print(root.value, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # ฟังก์ชัน postorder traversal
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.value, end=" ")

# สร้าง BinaryTree และเพิ่มค่าตามโครงสร้างที่ให้มา
bt = BinaryTree()

# เพิ่มค่าตามลำดับ
bt.insert(5)
bt.insert(3)
bt.insert(7)
bt.insert(2)
bt.insert(4)
bt.insert(8)

# แสดงผลการ traverse แบบต่างๆ
print("Inorder Traversal: ", end="")
bt.inorder(bt.root)  # จะแสดงค่าตามลำดับ Inorder: 2 3 4 5 7 8
print()

print("Preorder Traversal: ", end="")
bt.preorder(bt.root)  # จะแสดงค่าตามลำดับ Preorder: 5 3 2 4 7 8
print()

print("Postorder Traversal: ", end="")
bt.postorder(bt.root)  # จะแสดงค่าตามลำดับ Postorder: 2 4 3 8 7 5
print()
