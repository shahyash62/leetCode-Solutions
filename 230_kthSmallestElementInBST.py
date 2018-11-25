# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
	globalK = -1
	def kthSmallest(self, root, k):
		Solution.globalK = k
		return Solution.inorder(root).val
	
	def inorder(node):
		global globalK
		if(Solution.globalK == 0 or node == None):
			return node
		else:
			result = Solution.inorder(node.left)
			if(result != None): return result

			Solution.globalK -= 1
			if(Solution.globalK == 0): return node

			result = Solution.inorder(node.right)
			if(result != None): return result
