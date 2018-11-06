class Solution:
	def compareVersion(self, version1, version2):
		version1L = version1.split('.')
		version2L = version2.split('.')
		len1 = len(version1L)
		len2 = len(version2L)
		x = 0
		if(len1 > len2):
			while (x < len1-len2):
				version2L.append('0')
				x += 1
			len2 = len1
		elif(len1 < len2):
			while (x < len2-len1):
				version1L.append('0')
				x += 1
			len1 = len2
		x = 0
		print(version1L)
		print(version2L)
		while (x < len1 and x < len2):
			if(int(version1L[x]) > int(version2L[x])):
				return 1
			elif(int(version1L[x]) < int(version2L[x])):
				return -1
			x += 1
		return 0
