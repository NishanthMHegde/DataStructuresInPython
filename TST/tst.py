class Node(object):
	def __init__(self, character):
		self.character = character
		self.leftChild = None
		self.rightChild = None
		self.middleChild = None
		self.value = None

class TST(object):
	def __init__(self):
		self.root = None

	def put(self, key, value):
		self.root = self.put_item(self.root, key, value, 0)

	def put_item(self ,node, key, value, index):
		c = key[index]
		if not node:
			node = Node(c)

		if c < node.character:
			node.leftChild = self.put_item(node.leftChild, key, value, index)
		elif c > node.character:
			node.rightChild = self.put_item(node.rightChild, key, value, index)
		elif index < len(key) -1:
			node.middleChild = self.put_item(node.middleChild, key, value, index + 1)
		else:
			node.value = value
		return node 

	def get(self, key):
		node = self.get_item(self.root, key, 0)
		if not node:
			return None
		return node.value

	def get_item(self, node, key, index):
		if not node:
			return None
		c = key[index]
		if c < node.character:
			return self.get_item(node.leftChild, key, index)
		elif c > node.character:
			return self.get_item(node.rightChild, key, index)
		elif index < len(key) -1:
			return self.get_item(node.middleChild, key, index + 1)
		else:
			return node


tst = TST()
tst.put("cat", 23)
tst.put("car", 46)
tst.put("ox", 23)
tst.put("ball", 21)
tst.put("donkey", 2)

print(tst.get("cat"))
print(tst.get("car"))
print(tst.get("ox"))
print(tst.get("ball"))
print(tst.get("donkey"))
print(tst.get("dog"))