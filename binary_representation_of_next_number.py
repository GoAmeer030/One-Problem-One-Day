class Solution:
	def binaryNextNumber(self, s):
		# code here
		return bin(int(s,2)+1)[2:]