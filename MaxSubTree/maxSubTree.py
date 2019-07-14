# Python3 program to find the largest subtree 
# having identical left and right subtree 

# Helper class that allocates a new node 
# with the given data and None left and 
# right pointers. 
class newNode: 
	def __init__(self, data): 
		self.data = data 
		self.left = self.right = None

# Sets maxSize to size of largest subtree with 
# identical left and right. maxSize is set with 
# size of the maximum sized subtree. It returns 
# size of subtree rooted with current node. This 
# size is used to keep track of maximum size. 
def largestSubtreeUtil(root, Str, 
					maxSize, maxNode): 
	if (root == None): 
		return 0

	# string to store structure of left 
	# and right subtrees 
	left = [""] 
	right = [""] 

	# traverse left subtree and finds its size 
	ls = largestSubtreeUtil(root.left, left, 
							maxSize, maxNode) 

	# traverse right subtree and finds its size 
	rs = largestSubtreeUtil(root.right, right, 
							maxSize, maxNode) 

	# if left and right subtrees are similar 
	# update maximum subtree if needed (Note 
	# that left subtree may have a bigger 
	# value than right and vice versa) 
	size = ls + rs + 1
	if (left[0] == right[0]): 
		if (size > maxSize[0]): 
			maxSize[0] = size 
			maxNode[0] = root 

	# append left subtree data 
	Str[0] = Str[0] + "|" + left[0] + "|"

	# append current node data 
	Str[0] = Str[0] + "|" + str(root.data) + "|"

	# append right subtree data 
	Str[0] = Str[0] + "|" + right[0] + "|"

	return size 

# function to find the largest subtree 
# having identical left and right subtree 
def largestSubtree(node, maxNode): 
	maxSize = [0] 
	Str = [""] 
	largestSubtreeUtil(node, Str, maxSize, 
								maxNode) 

	return maxSize 

# Driver Code 
if __name__ == '__main__': 
	
	# Let us construct the following Tree 
	#	 50 
	#	 / \ 
	#	 10 60 
	# / \	 / \ 
	# 5 20 70 70 
	#		 / \ / \ 
	#		 65 80 65 80 
	root = newNode(50) 
	root.left = newNode(10) 
	root.right = newNode(60) 
	root.left.left = newNode(5) 
	root.left.right = newNode(20) 
	root.right.left = newNode(70) 
	root.right.left.left = newNode(65) 
	root.right.left.right = newNode(80) 
	root.right.right = newNode(70) 
	root.right.right.left = newNode(65) 
	root.right.right.right = newNode(80) 

	maxNode = [None] 
	maxSize = largestSubtree(root, maxNode) 

	print("Largest Subtree is rooted at node ", 
							maxNode[0].data) 
	print("and its size is ", maxSize) 

# This code is contributed by PranchalK 
