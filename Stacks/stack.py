class Stack(object):
	def __init__(self):
		self.stack = []
		self.size = 0

	def push(self, data):
		self.stack.append(data)
	
	def pop(self):
		if self.isEmpty():
			return None
		item = self.stack[-1]
		del self.stack[-1]
		return item

	def peek(self):
		return self.stack[-1]

	def isEmpty(self):
		if len(self.stack) == 0:
			return True
		else:
			return False

	def getSize(self):
		return len(self.stack)

	def printStack(self):
		print(self.stack)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.pop()
print("The stack is")
stack.printStack()
print("Top of stack is %s" % (stack.peek()))

print("Popping all items from the stack")
size = stack.getSize()
for i in range(size):
	print("Popped %s" % (stack.pop()))

print("Popped a null %s" % (stack.pop()))
