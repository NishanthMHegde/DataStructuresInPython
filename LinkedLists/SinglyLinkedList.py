
class Node(object):

	def __init__(self, data):
		self.data = data
		self.nextNode = None


class LinkedList(object):
	def __init__(self):
		self.head = None
		self.size = 0

	def insertAtBeginning(self, data):
		self.size = self.size + 1
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.head.nextNode = None
		else:
			new_node.nextNode = self.head
			self.head = new_node

	def insertAtEnd(self, data):
		self.size = self.size + 1
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.head.nextNode = None
		else:
			currentNode = self.head
			while currentNode.nextNode is not None:
				currentNode = currentNode.nextNode
			currentNode.nextNode = new_node

	def removeNode(self, data):
		if not self.head:
			return

		currentNode = self.head
		previousNode = None
		self.size = self.size - 1
		while currentNode.data != data:
			previousNode = currentNode
			currentNode = currentNode.nextNode

		if previousNode is None:
			self.head = currentNode.nextNode
		else:
			previousNode.nextNode = currentNode.nextNode


	def retrunSize(self):
		return self.size

	def getSize(self):
		size = 0
		currentNode = self.head
		while currentNode!= None:
			size = size + 1
			currentNode = currentNode.nextNode
		return size 

	def printList(self):
		currentNode = self.head
		while currentNode!= None:
			print(currentNode.data)
			currentNode = currentNode.nextNode
			


#trial

ll = LinkedList()
ll.insertAtBeginning(1)
ll.insertAtEnd(2)
ll.insertAtEnd(3)
ll.insertAtEnd(4)
ll.insertAtEnd(5)
ll.insertAtBeginning(0)
print("Printing the list")
ll.printList() #0,1,2,3,4,5
print("Size of the linked list is %s and %s" % (ll.retrunSize(), ll.getSize()))
ll.removeNode(0)
ll.removeNode(5)
print("Printing the list")
ll.printList() #1,2,3,4
print("Size of the linked list is %s and %s" % (ll.retrunSize(), ll.getSize()))