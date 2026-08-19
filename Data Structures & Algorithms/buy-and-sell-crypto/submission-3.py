class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max profit = min buying price, max selling price
        max_profit = 0
        buying = 0

        # when solving ex1 what do i do?
        # i'm moving my window forwrad so
        # ekeping buying at 10, moving selling forward
        # 10 -> 1
        # immediately i move my buying forward too because 
        for selling in range(1, len(prices)):
            if prices[buying] < prices[selling]:
                max_profit = max(max_profit, prices[selling] - prices[buying])

            else:
                buying = selling

        return max_profit
        # testing this on prices
        # buying = 10, selling = 1
        # max profit = -9 which doesnt count
        # buying < selling so setting buying to be buying + 1
        # next: buying = 1, selling = 5
        # max profit = 4
        # buying is not < selling
        # next: buying = 1, selling = 6
        # ok
        # next buying = 1, selling = 