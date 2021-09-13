# 골드3 - 앱
# dp


# 냅색(bounded) 응용
# 메모리 값은 m이상이어야 하므로 메모리값을 고정시키는 것이 아닌
# 비용을 고정시킨 후 dp 수행
# 하나의 앱은 하나만 삭제 가능하므로 unbouned따라서 한다
# c<=100 이라해서 범위가 100이 아니라 100(갯수)*100(값) = 10000이 최대.

# 메모리, 비용
#           0  1  2   3   4   5   6  ... 10000
# 30 3      0  0  0  30  30  30  30  ...    30
# 10 0      10 10 10 40  40  40  40  ...    40
# ...


n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
total = [(memory[i], cost[i]) for i in range(n)]
dp = [0]*10001

for tot in total:
    mem, cst = tot
    for i in range(10000, cst-1, -1):
        dp[i] = max(dp[i-cst]+mem, dp[i])

for i in range(10001):
    if dp[i] >= m:
        print(i)
        break
