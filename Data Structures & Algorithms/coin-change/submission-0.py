from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for current_amount in range(1, amount + 1):
            for coin in coins:
                if coin <= current_amount:
                    remaining = current_amount - coin
                    dp[current_amount] = min(
                        dp[current_amount],
                        dp[remaining] + 1
                    )
        
        return dp[amount] if dp[amount] <= amount else -1

        