class Solution:
    def minimumCost(self, n : int, w : int, cost : List[int]) -> int:
        dp=[[-1 for _ in range(w+1)] for _ in range(n+1)]
        def helper(i,w):
            if i==n:
                if w==0:
                    return 0
                return 10000000000
            if w<0:
                return 10000000
            if dp[i][w]!=-1:
                return dp[i][w]
            take=0
            if cost[i]!=-1:
                take=cost[i]+helper(i,w-(i+1))
            skip=helper(i+1,w)
            dp[i][w]=min(take,skip)
            return dp[i][w]
        return helper(0,w)