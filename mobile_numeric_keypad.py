class Solution:
	def getCount(self, N):
		# code here
		dp = [[0] * 10 for _ in range(N + 1)]
 
        data = [[0, 8], [1, 2, 4], [1, 2, 3, 5], [2, 3, 6], 
                [1, 4, 5, 7], [2, 4, 5, 6, 8], [3, 5, 6, 9], 
                [4, 7, 8], [5, 7, 8, 9, 0], [6, 8, 9]]
     
        for i in range(1, N + 1):
            for j in range(10):
                if i == 1:
                    dp[i][j] = 1
                else:
                    for prev in data[j]:
                        dp[i][j] += dp[i - 1][prev]
     
        sum = 0
        for j in range(10):
            sum += dp[N][j]
     
        return sum
