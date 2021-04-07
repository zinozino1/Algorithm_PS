# 스택,큐 -> 절대 못품
# 분명 o(n^2)인데 풀리네..


def solution(prices):

    res = [0] * len(prices)
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[j] < prices[i]:
                break

        res[i] = cnt

    return res
