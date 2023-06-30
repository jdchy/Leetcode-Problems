
import math

def maxProfit(prices):

    min_price = math.inf
    max_profit = 0
    for index in range(len(prices)):
        if prices[index] < min_price:
            min_price = prices[index]
            print('Min -->'+str(min_price))
        elif prices[index] - min_price > max_profit:
            max_profit = prices[index] - min_price
            print('Max -->'+str(max_profit))
    return max_profit


if __name__ == '__main__':
	print(maxProfit([7,6,4,3,1,5,7]))