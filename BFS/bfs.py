class Node(object):
	def __init__(self, name):
		self.name = name
		self.neighbours = []
		self.visited =False


class BFS(object):
	def bfs(self, starting_node):
		queue = []
		starting_node.visited = True
		print(starting_node.name)
		queue.append(starting_node)

		while queue:
			node = queue.pop(0)
			
			for n in node.neighbours:
				if n.visited is False:
					n.visited = True
					print(n.name)
					queue.append(n)

node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')
node6 = Node('F')

node1.neighbours.append(node2)
node1.neighbours.append(node3)
node2.neighbours.append(node4)
node2.neighbours.append(node5)
node3.neighbours.append(node6)

bfs = BFS()
bfs.bfs(node1)
