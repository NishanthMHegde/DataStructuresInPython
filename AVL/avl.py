class Node(object):
    def __init__(self, data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None

class AVL(object):
    def __init__(self):
        self.root = None


    def calcHeight(self, node):
        if not node:
            return -1
        return node.height

    def calcBalance(self, node):
        if not node:
            return 0
        return self.calcHeight(node.leftChild) - self.calcHeight(node.rightChild)

    def rightRotation(self, node):
        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild

        tempLeftChild.rightChild = node
        node.leftChild = t

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild) ) + 1
        tempLeftChild.height = max(self.calcHeight(tempLeftChild.leftChild), self.calcHeight(tempLeftChild.rightChild)) + 1
        return tempLeftChild

    def leftRotation(self, node):
        tempRightChild = node.rightChild
        t = tempRightChild.leftChild

        tempRightChild.leftChild = node
        node.rightChild = t
        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild) ) + 1
        tempRightChild.height = max(self.calcHeight(tempRightChild.leftChild), self.calcHeight(tempRightChild.rightChild)) + 1
        return tempRightChild

    def insert(self, data):
        self.root = self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if not node:
            self.root = Node(data)
            return self.root

        if data <node.data:
            node.leftChild = self.insert_node(data, node.leftChild)
        else:
            node.rightChild = self.insert_node(data, node.rightChild)

        node.height = max(self.calcHeight(node.leftChild), self.calcHeight(node.rightChild)) + 1
        balance = self.calcBalance(node)
        
        #left left heavy situation
        if balance > 1 and data < node.leftChild.data:
            print("Carrying out right right rotation at node %s" % (node.data))
            node = self.rightRotation(node)
        #right right heavy situation
        elif balance < -1 and data > node.rightChild.data:
            print("Carrying out left left rotation at node %s" % (node.data))
            node = self.leftRotation(node)
        #left right heavy situation
        elif balance > 1 and data > node.leftChild.data:
            print("Carrying out left rotation at node %s" % (node.leftChild.data))
            node.leftChild = self.leftRotation(node.leftChild)
            print("Carrying out right rotation at node %s" % (node.data))
            node = self.rightRotation(node)
        #right left heavy situation
        elif balance < -1 and data < node.rightChild.data:
            print("Carrying out right rotation at node %s" % (node.rightChild.data))
            node.rightChild = self.rightRotation(node.rightChild)
            print("Carrying out left rotation at node %s" % (node.data))
            node = self.leftRotation(node)
        return node

    def inorder(self):
        if self.root:
            self.inorder_traversal(self.root)

    def inorder_traversal(self, node):
        if node.leftChild:
            self.inorder_traversal(node.leftChild)
        print(node.data)
        if node.rightChild:
            self.inorder_traversal(node.rightChild)


avl = AVL()
avl.insert(10)
avl.insert(20)
avl.insert(30)
print("Traversing the tree")
avl.inorder()

avl = AVL()
avl.insert(30)
avl.insert(20)
avl.insert(10)
print("Traversing the tree")
avl.inorder()

avl = AVL()
avl.insert(30)
avl.insert(5)
avl.insert(35)
avl.insert(32)
avl.insert(40)
avl.insert(45)
print("Traversing the tree")
avl.inorder()