
class HashTables(object):
	def __init__(self):
		self.size = 10
		self.keys = [None] * self.size
		self.values = [None] * self.size

	def put(self, key, data):
		index = self.hash_function(key)
		while self.keys[index] != None:
			if self.keys[index] == key:
				self.values[index] = data
				return
			index = (index + 1) % self.size

		self.keys[index] = key
		self.values[index] = data

	def get(self, key):
		index = self.hash_function(key)
		while self.keys[index] != None:
			if self.keys[index] == key:
				return self.values[index]
			index = (index + 1) % self.size

		return None

	def hash_function(self, key):
		sum = 0
		for i in range(len(key)):
			sum = sum + ord(key[i])
		return sum%self.size


hashtable = HashTables()
hashtable.put("apple", 10)
hashtable.put("cat", 20)
hashtable.put("dog", 30)
hashtable.put("orange", 40)

print(hashtable.get("apple"))
print(hashtable.get("cat"))
print(hashtable.get("dog"))
print(hashtable.get("orange"))
print(hashtable.get("strawberry"))