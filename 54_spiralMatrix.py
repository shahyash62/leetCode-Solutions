class Solution:
	def spiralOrder(self, matrix):
		totalRows = len(matrix)
		if(totalRows == 0): return []
		totalCols = len(matrix[0])
		total = totalRows * totalCols
		result = []
		dJR = 0
		dJL = -1
		dID = 0
		dIU = -1
		i = 0
		j = 0
		while(len(result) < total):
			while(j < totalCols - dJR and len(result) < total):
				result.append(matrix[i][j])
				j += 1
			dIU += 1
			j -= 1
			i += 1
			while(i < totalRows - dID and len(result) < total):
				result.append(matrix[i][j])
				i += 1
			dJR += 1
			i -= 1
			j -= 1
			while(j > dJL and len(result) < total):
				result.append(matrix[i][j])
				j -= 1
			dID += 1
			j += 1
			i -= 1
			while(i > dIU and len(result) < total):
				result.append(matrix[i][j])
				i -= 1
			dJL += 1
			i += 1
			j += 1
			print('{0}i  {1}j'.format(i,j))
		return (result)
