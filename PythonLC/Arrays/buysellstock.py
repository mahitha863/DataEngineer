

class Solution:
    def maxProfit(self, prices: list[int]) -> list[int]:
        """profit = 0
        minp = prices[0]
        #for price in prices:
            #if price < minp:
                #minp = price
            #if price - minp > profit:
                #profit = price - minp
        for price in prices:
            minp = min(price, minp)
            profit = max(price - minp, profit)
        return profit"""

        # Sliding window method
        profit = 0
        buy,sell = 0,1
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = max(prices[sell] - prices[buy], profit)
            else:
                buy = sell
            sell += 1

        return profit 


    def maxProfit2(self, prices: list[int]) -> list[int]:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
        
        


if __name__ == "__main__":
    buysell = Solution()

    # Buy and sell stock I - only one transaction allowed (one buy and sell)
    if buysell.maxProfit([7,1,5,3,6,4]) == 5:
        print("Testcase1: Passed")
    else:
        print("Testcase1: Failed")
    
    if buysell.maxProfit([7,6,4,3,1]) == 0:
        print("Testcase2: Passed")
    else:
        print("Testcase2: Failed")
    
    if buysell.maxProfit([7,2,6,5,1,8,2]) == 7:
        print("Testcase3: Passed")
    else:
        print("Testcase3: Failed")

    # Buy and sell stock II - multiple transactions allowed (multiple buy and sell)
    if buysell.maxProfit2([7,1,5,3,6,4]) == 7:
        print("Testcase1: Passed")
    else:
        print("Testcase1: Failed")
    
    if buysell.maxProfit2([7,6,4,3,1]) == 0:
        print("Testcase2: Passed")
    else:
        print("Testcase2: Failed")
    
    if buysell.maxProfit2([7,2,6,5,1,8,2]) == 11:
        print("Testcase3: Passed")
    else:
        print("Testcase3: Failed")

    if buysell.maxProfit2([1,2,3,4,5]) == 4:
        print("Testcase4: Passed")
    else:
        print("Testcase4: Failed")

