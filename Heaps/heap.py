class Heap(object):
	HEAP_SIZE = 10

	def __init__(self):
		self.currentPosition = -1
		self.heap = [0] * Heap.HEAP_SIZE

	def insert(self, data):
		if self.isFull():
			print("Heap is full")
			return
		self.currentPosition = self.currentPosition + 1
		self.heap[self.currentPosition] = data
		self.fixUp(self.currentPosition)

	def fixUp(self, index):
		parentIndex = int((index-1)/2)
		while (parentIndex >=0) and (self.heap[parentIndex] < self.heap[index]):
			temp = self.heap[parentIndex]
			self.heap[parentIndex] = self.heap[index]
			self.heap[index] = temp
			parentIndex = int((index-1)/2)

	def heapsort(self):
		for i in range(0, self.currentPosition + 1):
			temp = self.heap[0]
			print("Root node is %s" % (temp))
			self.heap[0] = self.heap[self.currentPosition -i]
			self.heap[self.currentPosition -i] = temp
			self.fixDown(0, self.currentPosition -i -1)

	def fixDown(self, index, upto):
		while index <= upto:
			leftChild = 2*index + 1
			rightChild = 2*index + 2

			if leftChild < upto:
				childToSwap = None
				if rightChild > upto:
					childToSwap = leftChild
				else:
					if self.heap[leftChild] > self.heap[rightChild]:
						childToSwap = leftChild
					else:
						childToSwap = rightChild
				if self.heap[index] < self.heap[childToSwap]:
					temp = self.heap[index]
					self.heap[index] = self.heap[childToSwap]
					self.heap[childToSwap] = temp
				else:
					break
				index = childToSwap
			else:
				break
	def isFull(self):
		if self.currentPosition == Heap.HEAP_SIZE:
			return True
		else:
			return False



heap = Heap()
heap.insert(10)
heap.insert(-20)
heap.insert(0)
heap.insert(2)

heap.heapsort()