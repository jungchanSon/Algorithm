class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [i for i in range(n+1)]
        for i in range(n+1):
            tmp = bin(dp[i])
            c = tmp.count('1')
            print(tmp, c)
            if c < 0:
                dp[i] = 0 
            else:
                dp[i] = c
        return dp