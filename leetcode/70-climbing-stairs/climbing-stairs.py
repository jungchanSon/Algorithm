class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(45)]
        dp[0] =1
        dp[1] =2
        
        for i in range(2, 45):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n-1]