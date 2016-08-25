class BST:
	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self):
		return "Tree with root %s"% self.value


	''' Tree Traversal '''

	def DFS(node): # Starts with the root node
		if not node:
			None

		r = []

		if node.left:
			r += DFS(node.left)

		if node.value:
			r.append(node.value) # Add the node value at each level

		if node.right:
			r += DFS(node.right)

		return r

	def BFS(node):
		r = []
		nodelist = [node]
		while nodelist:
			next_node = []
			for subnode in nodelist:
				r.append(subnode.value)
				if subnode.left:
					next_node.append(subnode.left)
				if subnode.right:
					next_node.append(subnode.right)

			nodelist = next_node # All the nodes are visited

		return nodelist



	def insert(node, value):
    	if not node.value:
        	node.value = value

    	if value < node.value:
        	node.left = node.left or Node()
        	insert(node.left, value)

    	elif value > node.value:
        	node.right = node.right or Node()
        	insert(node.right, value)

    def inorder(node):
    	if node is not None:
    		inorder(node.left)
    		print node.value
    		inorder(node.right)

   	def minvalue(node):
   		current = node
   		while current.left is not None:
   			current = current.left
   		return current

   	def delete(node, value):
   		if node is None:
   			return node

   		if value < node.value:
   			delete(node.left, value)

   		elif value > node.value:
   			delete(node.right, value)

   		else:

   			if node.left is None:
   				t = node.right
   				node.left = None
   				return t

   			elif node.right is None:
   				t = node.left
   				node.right = None
   				return t

   			temp = minvalue(node.right) # Get the inorder successor of the node. 

   			node.value = temp.value

   			delete(node.right, temp.value)

   		return root