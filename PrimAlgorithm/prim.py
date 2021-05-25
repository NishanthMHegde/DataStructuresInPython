import heapq

class Vertex(object):
	def __init__(self, name):
		self.name = name
		self.neighbours = []


class Edge(object):
	def __init__(self, weight, startVertex, endVertex):
		self.weight = weight
		self.startVertex = startVertex
		self.endVertex = endVertex

	def __cmp__(self, other):
		return self.cmp(self.weight, other.weight)

	def __lt__(self, other):
		return self.weight < other.weight


class Prim(object):
	def __init__(self, vertexList):
		self.vertexList = vertexList
		self.spanningTree = []
		self.edgeHeap = []
		self.totalCost = 0

	def prim(self, vertex):

		self.vertexList.remove(vertex)
		while self.vertexList:
			for edge in vertex.neighbours:
				if edge.endVertex in self.vertexList:
					heapq.heappush(self.edgeHeap, edge)

			edge = heapq.heappop(self.edgeHeap)
			self.spanningTree.append(edge)
			self.vertexList.remove(edge.endVertex)
			vertex = edge.endVertex
			self.totalCost = self.totalCost + edge.weight

	def spanningTreeInfo(self):
		for edge in self.spanningTree:
			print("%s ---- %s" % (edge.startVertex.name, edge.endVertex.name))
		print("Total Cost is %s" % (self.totalCost))

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
edge8 = Edge(1, vertex2, vertex1)
edge9 = Edge(3, vertex3, vertex2)
edge10 = Edge(7, vertex3, vertex1)
edge11 = Edge(10, vertex4, vertex1)
edge12 = Edge(4, vertex4, vertex3)
edge13 = Edge(5, vertex5, vertex1)
edge14 = Edge(2, vertex5, vertex4)



vertex1.neighbours.append(edge1)
vertex1.neighbours.append(edge3)
vertex1.neighbours.append(edge4)
vertex1.neighbours.append(edge6)
vertex2.neighbours.append(edge2)
vertex2.neighbours.append(edge8)
vertex3.neighbours.append(edge5)
vertex3.neighbours.append(edge9)
vertex3.neighbours.append(edge10)
vertex4.neighbours.append(edge7)
vertex4.neighbours.append(edge11)
vertex4.neighbours.append(edge12)
vertex5.neighbours.append(edge13)
vertex5.neighbours.append(edge14)
vertexList = [vertex1, vertex2, vertex3, vertex4, vertex5]

prim = Prim(vertexList)
prim.prim(vertex1)
prim.spanningTreeInfo()