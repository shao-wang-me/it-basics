from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy_prices = []
        sell_prices = []
        buy_backlog = {}
        sell_backlog = {}
        for price, amount, order_type in orders:
            if order_type == 0:
                # buy
                while amount and sell_prices and sell_prices[0] <= price:
                    sell_price = sell_prices[0]
                    sell_amount = sell_backlog[sell_price]
                    if sell_amount > amount:
                        sell_backlog[sell_price] = sell_amount - amount
                        amount = 0
                    else:
                        sell_backlog.pop(sell_price)
                        sell_prices = sell_prices[1:]
                        amount -= sell_amount
                if amount:
                    if price in buy_backlog:
                        buy_backlog[price] = buy_backlog[price] + amount
                    else:
                        buy_backlog[price] = amount
                        buy_prices.append(price)
                        buy_prices.sort()
            else:
                # sell
                while amount and buy_prices and buy_prices[-1] >= price:
                    buy_price = buy_prices[-1]
                    buy_amount = buy_backlog[buy_price]
                    if buy_amount > amount:
                        buy_backlog[buy_price] = buy_amount - amount
                        amount = 0
                    else:
                        buy_backlog.pop(buy_price)
                        buy_prices = buy_prices[:-1]
                        amount -= buy_amount
                if amount:
                    if price in sell_backlog:
                        sell_backlog[price] = sell_backlog[price] + amount
                    else:
                        sell_backlog[price] = amount
                        sell_prices.append(price)
                        sell_prices.sort()

        ans = 0
        for x in buy_backlog:
            ans += buy_backlog[x]
        for x in sell_backlog:
            ans += sell_backlog[x]

        return ans % (10 ** 9 + 7)


def test(cases):
    for orders in cases:
        solution = Solution()
        print(solution.getNumberOfBacklogOrders(orders))


test([
    # 6
    [[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]],
    # 999999984
    [[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]],
    # 22
    [[1, 29, 1], [22, 7, 1], [24, 1, 0], [25, 15, 1], [18, 8, 1], [8, 22, 0], [25, 15, 1], [30, 1, 1], [27, 30, 0]],
    # 83062672
    [[944925198, 885003661, 0], [852263791, 981056352, 0], [16300530, 415829909, 0], [940927944, 713835606, 0],
     [606389372, 407474168, 1], [139563740, 85382287, 1], [700244880, 901922025, 1], [972900669, 15506445, 0],
     [576578542, 65339074, 0], [45972021, 293765308, 0], [464403992, 97750995, 0], [29659852, 536508041, 0],
     [799523481, 299864737, 0], [711908211, 480514887, 1], [354125407, 677598767, 1], [279004011, 688916331, 0],
     [263524013, 64622178, 0], [375395974, 460070320, 0], [971786816, 379275200, 1], [577774472, 214070125, 1],
     [987757349, 711231195, 0]]
])
