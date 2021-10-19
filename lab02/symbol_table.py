class Node:

	def __init__(self, key):
		self.key = key
		self.next = None

class SymbolTable:

	def __init__(self):
		self.size = 10
		self.st = [None] * self.size

	def hash(self, key):
		h = 0
		for c in key:
			h += ord(c)
			h = h % self.size
		return h

	def search(self, key):
		index = self.hash(key)
		node = self.st[index]
		l_index = 0
		while node is not None and node.key != key:
			node = node.next
			l_index += 1
		if node is None:
			return None
		else:
			return (index, l_index)

	def pos(self, key):

		found = self.search(key)
		if found is not None:
			return found

		index = self.hash(key)
		node = self.st[index]

		if node is None:
			self.st[index] = Node(key)
			return (index, 0)

		l_index = 0
		prev = node
		while node is not None:
			prev = node
			node = node.next
			l_index += 1

		prev.next = Node(key)
		return (index, l_index)