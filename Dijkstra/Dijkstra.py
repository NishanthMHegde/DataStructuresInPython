import sys
import heapq

class Node(object):
	def __init__(self, name):
		self.name = name
		self.neighbours = []
		self.predecessor = None
		self.minDistance = sys.maxsize

	def __cmp__(self, other):
		return self.cmp(self.minDistance, other.minDistance)

	def __lt__(self, other):
		return self.minDistance < other.minDistance


class Edge(object):
	def __init__(self, weight, startVertex, endVertex):
		self.weight = weight
		self.startVertex = startVertex
		self.endVertex = endVertex


class Dijsktra(object):

	def dijkstra(self, startingVertex):
		q = []
		startingVertex.minDistance = 0
		heapq.heappush(q, startingVertex)

		while q:
			targetVertex = heapq.heappop(q)
			for edge in targetVertex.neighbours:
				u = edge.startVertex
				v = edge.endVertex

				newDistance = u.minDistance + edge.weight
				if newDistance < v.minDistance:
					v.minDistance = newDistance
					v.predecessor = u
					heapq.heappush(q, v)

	def shortest_path(self, targetVertex):
		print("The shortest path to the target vertex %s is %s" % (targetVertex.name, targetVertex.minDistance))
		node = targetVertex
		while node is not None:
			print(node.name)
			node = node.predecessor

nodeS = Node('S')
nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')
nodeE = Node('E')

edge1 = Edge(1, nodeS, nodeA)
edge2 = Edge(5, nodeS, nodeB)
edge3 = Edge(2, nodeA, nodeB)
edge4 = Edge(1, nodeA, nodeD)
edge5 = Edge(2, nodeB, nodeD)
edge6 = Edge(2, nodeA, nodeC)
edge7 = Edge(3, nodeC, nodeD)
edge8 = Edge(1, nodeC, nodeE)
edge9 = Edge(2, nodeD, nodeE)

nodeS.neighbours.append(edge1)
nodeS.neighbours.append(edge2)
nodeA.neighbours.append(edge3)
nodeA.neighbours.append(edge4)
nodeA.neighbours.append(edge6)
nodeB.neighbours.append(edge5)
nodeC.neighbours.append(edge7)
nodeC.neighbours.append(edge8)
nodeD.neighbours.append(edge9)

dijkstra = Dijsktra()
dijkstra.dijkstra(nodeS)
dijkstra.shortest_path(nodeE)