class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None 

class BST(object):
    def __init__(self):
        self.root = None


    def insert(self, data):
        if self.root:
            self.insertNode(data, self.root)
        else:
            new_node = Node(data)
            self.root = new_node

    def insertNode(self, data, node):
        if data < node.data:
            if node.leftChild:
                self.insertNode(data, node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data, node.rightChild)
            else:
                node.rightChild = Node(data)

    def inorder(self):
        if self.root:
            self.inorder_traversal(self.root)

    def inorder_traversal(self, node):
        if node.leftChild:
            self.inorder_traversal(node.leftChild)
        print(node.data)
        if node.rightChild:
            self.inorder_traversal(node.rightChild)

    def getMax(self):
        if self.root:
            return self.getMaxValue(self.root)
        else:
            return None
    def getMaxValue(self, node):
        if node.rightChild:
            return self.getMaxValue(node.rightChild)
        return node.data

    def getMin(self):
        if self.root:
            return self.getMinValue(self.root)
        else:
            return None
    def getMinValue(self, node):
        if node.leftChild:
            return self.getMinValue(node.leftChild)
        return node.data


    def remove(self, data):
        if not self.root:
            return None
        if self.root:
            self.root = self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if not node:
            return None
        if data < node.data:
            node.leftChild = self.remove_node(data, node.leftChild)
        elif data > node.data:
            node.rightChild = self.remove_node(data, node.rightChild)
        else:
            #we found the node we are looking for

            #node is a leaf node
            if (node.leftChild == None) and (node.rightChild == None):
                del node
                return None

            #it has right child only
            if node.leftChild == None:
                temp = node.rightChild
                del node
                return temp 
            #it has left child only
            elif node.rightChild == None:
                temp = node.leftChild
                del node
                return temp 
            #has both left and right children: get the predecessory of the node from left sub tree
            tempNode = self.get_predecessor(node.leftChild)
            node.data = tempNode.data
            node.leftChild = self.remove_node(tempNode.data, node.leftChild)

        return node

    def get_predecessor(self, node):
        if node.leftChild:
            return self.get_predecessor(node.leftChild)
        return node




bst = BST()

bst.insert(12)
bst.insert(11)
bst.insert(10)
bst.insert(14)
bst.insert(24)
bst.insert(19)
bst.insert(17)
bst.insert(45)
bst.insert(67)
bst.insert(56)
bst.insert(34)
print("Inorder traverse result")
bst.inorder()

print("Minimum value in the tree %s" % (bst.getMin()))
print("Maximum value in the tree %s" % (bst.getMax()))

print("Deleting 24 and 56")
bst.remove(24)
bst.remove(56)

#printing again 
print("Inorder traverse result")
bst.inorder()

print("Minimum value in the tree %s" % (bst.getMin()))
print("Maximum value in the tree %s" % (bst.getMax()))