class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        curr=prices[0]
        for i in range(1,len(prices)):
            if curr < prices[i]:
                maxi = max(maxi, prices[i]-curr)
            else:
                curr=prices[i]
        return maxi
        
