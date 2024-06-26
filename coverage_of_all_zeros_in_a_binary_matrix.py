class Solution:
	def findCoverage(self, matrix):
	    res = 0
	    for i in range(len(matrix)):
	        for j in range(len(matrix[0])):
	            if matrix[i][j] == 0:
	                if j-1 > -1 and matrix[i][j-1] == 1:
	                    res += 1
	                if j+1 < len(matrix[0]) and matrix[i][j+1] == 1:
	                    res += 1
	                if i-1 > -1 and matrix[i-1][j] == 1:
	                    res += 1
	                if i+1 < len(matrix) and matrix[i+1][j] == 1:
	                    res += 1
        return res
