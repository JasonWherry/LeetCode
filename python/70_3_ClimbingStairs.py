dp = dict()
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        if dp.get(n) is not None:
            return dp.get(n)
        dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return dp[n]