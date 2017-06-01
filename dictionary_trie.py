# marker is the address of nodes on the table
# a node having a tag implies path from root to that node is a valid word

table = {}
marker = 0

class Node:
	global table
	global marker
	data = ''
	child = None
	sibling = None
	tag = None
	
	def add(self, new_data, tag):
		index = -1
		if new_data[0] != self.data[0]:
			if self.sibling != None:
				sibling_object = table[self.sibling]
				return sibling_object.add(new_data,tag)
			else:
				self.sibling = marker
				sibling_object = Node()
				sibling_object.data = new_data
				table[marker] = sibling_object
				marker += 1
				self.tag = tag
				return tag+1
		for i in range(len(self.data)):
			if self.data[i] != new_data[i]:
				index = i
				break
		if index != -1:
			data1 = self.data[index:]
			data2 = new_data[index:]
			self.data = self.data[:index]
			self_tag = self.tag
			self.tag = None
			if self.child != None:
				child_object = table[self.child]
				child_object.add(data1,self_tag)
				return child_object.add(data2,tag)
			else:
				self.child = marker
				child_object = Node()
				child_object.data = data1
				child_object.tag = self_tag
				table[self.child] = child_object
				marker += 1
				return child_object.add(data2,tag)
		else:
			self.tag = tag
			return tag+1

class Dictionary:
	root = None
	tag = 0

	def update_table(self):
		global table, marker
		table = pickle.load(open('english.chow','rb'))
		marker = pickle.load(open('marker.chow','rb'))

	def addWord(self,word):
		global marker, table
		if self.root == None:
			self.root = Node()
			self.root.data = word
			table[marker] = self.root
			marker += 1
			self.root.tag = tag
			self.tag += 1
		else:
			self.tag = self.root.add(word,self.tag)
	
	def addWord2(self, word):
		self.update_table()
		self.addWord(word)