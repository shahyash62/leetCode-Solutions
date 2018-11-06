class Solution:
	def validIPAddress(self, IP):
		if('.' in IP and Solution.validIPv4(IP)):
			return 'IPv4'
		elif(':' in IP and Solution.validIPv6(IP)):
			return 'IPv6'
		else:
			return 'Neither'

	def validIPv4(ip):
		splitIp = ip.split('.')
		validChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		if (len(splitIp) != 4):
			return False
		for x in splitIp:
			if(x == ''):
				return False
			if(x[0] == '0' and len(x) > 1):
				return False
			for y in x:
				if(y not in validChars):
					return False
			try:
				if(int(x) > 255 or int(x) < 0):
					return False
			except:
				return False
		return True

	def validIPv6(ip):
		splitIp = ip.split(':')
		validChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
		if (len(splitIp) != 8):
			return False
		for x in splitIp:
			if(x == ''):
				return False
			if(len(x) > 4):
				return False
			for y in x.lower():
				if(y not in validChars):
					return False
		return True
