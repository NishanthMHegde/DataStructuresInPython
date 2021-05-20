class Queue(object):
	def __init__(self):
		self.queue = []

	def enqueue(self, data):
		self.queue.append(data)

	def isEmpty(self):
		if len(self.queue) == 0:
			return True
		else:
			return False
	def dequeue(self):
		if self.isEmpty():
			return None
		item = self.queue[0]
		del self.queue[0]
		return item

	def printQueue(self):
		print(self.queue)

	def getSize(self):
		return len(self.queue)


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.printQueue()

size = queue.getSize()
for i in range(size):
	print("Dequeued %s" % (queue.dequeue()))

print("Dequeued None %s" % (queue.dequeue()))