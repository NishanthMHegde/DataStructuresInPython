class Node(object):
	def __init__(self, name):
		self.name = name
		self.neighbours = []
		self.visited =False

class DFS(object):

	def dfs(self, starting_node):
		starting_node.visited = True
		print(starting_node.name)

		for n in starting_node.neighbours:
			if n.visited is False:
				self.dfs(n)


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

dfs = DFS()
dfs.dfs(node1)