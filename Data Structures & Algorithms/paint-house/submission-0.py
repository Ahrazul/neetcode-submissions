class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [0, 0, 0]

        for i in range(n):
            red = costs[i][0] + min(dp[1], dp[2])
            blue = costs[i][1] + min(dp[0], dp[2]) 
            green = costs[i][2] + min(dp[0], dp[1])

            dp = [red, blue, green]


        return min(dp)        