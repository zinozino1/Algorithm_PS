# 풀이시간 : 20분


# 내 풀이 - > 슬라이딩 윈도우 풀이
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lt, rt = 0, 1
        max_price = -1e9
        while rt <= len(prices)-1:
            if prices[rt]-prices[lt] < 0:
                lt, rt = rt, rt+1
            else:
                if prices[rt]-prices[lt] > max_price:
                    max_price = prices[rt]-prices[lt]
                rt += 1
        return 0 if max_price == -1e9 else max_price


# 답 -> 카데인 알고리즘 -> max, min을 계속해서 갱신
# 이해가가지 않으면 그래프를 그려 판단해볼 것

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_n = 1e9
        profit = 0
        for price in prices:
            min_n = min(price, min_n)
            profit = max(profit, price-min_n)

        return profit
