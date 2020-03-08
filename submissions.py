class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount==0:
            return 1
        res=[0]*(amount+1)
        res[0]=1
        for coin in (coins):
            for j in range(1,amount+1):
                if (j>=coin):
                    res[j]=res[j]+res[j-coin]
        return res[amount]
