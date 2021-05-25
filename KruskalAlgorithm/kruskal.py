class Vertex(object):
	def __init__(self, name):
		self.name = name
		self.node = None


class Node(object):
	def __init__(self, height, nodeId, parentNode):
		self.height = height
		self.nodeId = nodeId
		self.parentNode = parentNode

class Edge(object):
	def __init__(self, weight, startVertex, endVertex):
		self.weight = weight
		self.startVertex = startVertex
		self.endVertex = endVertex

	def __cmp__(self, other):
		return self.cmp(self.weight, other.weight)

	def __lt__(self, other):
		return self.weight < other.weight

class Disjoint(object):
	def __init__(self, vertexList):
		self.nodeCount = 0
		self.setCount = 0
		self.rootNodes = []
		self.vertexList = vertexList
		self.makeSets(vertexList)

	def makeSets(self, vertexList):
		for vertex in vertexList:
			self.makeSet(vertex)

	def makeSet(self, vertex):
		node = Node(0, len(self.rootNodes), None)
		vertex.node = node
		self.rootNodes.append(node)
		self.setCount = self.setCount + 1
		self.nodeCount = self.nodeCount + 1

	def find(self, node):

		#find the parent of the node which will be the root of the tree
		currentNode = node
		while currentNode.parentNode is not None:
			currentNode = currentNode.parentNode
		root = currentNode

		#now flatten the tree by making all the nodes of a tree directly the children of the root
		currentNode = node
		while currentNode is not root:
			temp = currentNode.parentNode
			currentNode.parentNode = root
			currentNode = temp
		return root.nodeId

	def merge(self, node1, node2):
		index1 = self.find(node1)
		index2 = self.find(node2)

		#if both have same root nodeId index, it means they are in same set
		if index1==index2:
			return

		#we merge the two trees.
		#the small tree will attach itself to the bigger tree
		root1 = self.rootNodes[index1]
		root2 = self.rootNodes[index2]

		if root1.height < root2.height:
			root1.parentNode = root2
		elif root2.height < root1.height:
			root2.parentNode = root1
		else:
			root2.parentNode = root1
			root1.height = root1.height + 1 #height of tree changes only when 2 same size trees attah themselves

class Kruskal(object):
	def spanningTrees(self, edgeList, vertexList):
		disjoint = Disjoint(vertexList)
		self.edgeList = edgeList
		self.spanningTrees = []
		self.totalCost = 0

		#sort the  edges
		self.edgeList.sort()

		for edge in self.edgeList:
			u = edge.startVertex
			v = edge.endVertex

			#check the parent nodes are disjoint
			if disjoint.find(u.node) is not disjoint.find(v.node):
				disjoint.merge(u.node, v.node)
				self.spanningTrees.append(edge)
				self.totalCost = self.totalCost + edge.weight

		for edge in self.spanningTrees:
			print("%s ---- %s" % (edge.startVertex.name, edge.endVertex.name))
		print("Total cost of the spanning tree is %s" % (self.totalCost))


vertex1 = Vertex('A')
vertex2 = Vertex('B')
vertex3 = Vertex('C')
vertex4 = Vertex('D')
vertex5 = Vertex('E')

edge1 = Edge(1, vertex1, vertex2)
edge2 = Edge(3, vertex2, vertex3)
edge3 = Edge(7, vertex1, vertex3)
edge4 = Edge(10, vertex1, vertex4)
edge5 = Edge(4, vertex3, vertex4)
edge6 = Edge(5, vertex1, vertex5)
edge7 = Edge(2, vertex4, vertex5)

vertexList = [vertex1, vertex2, vertex3, vertex4, vertex5]
edgeList = [edge1, edge2, edge3, edge4, edge5, edge6, edge7]

kruskal = Kruskal()
kruskal.spanningTrees(edgeList, vertexList)

