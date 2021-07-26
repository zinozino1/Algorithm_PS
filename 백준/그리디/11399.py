# 실버3 - ATM
# 그리디

# dfs? n=1000 최악의 경우 1000!
# dp vs 그리디


n = int(input())
p = list(map(int, input().split()))
p.sort()
res = 0
for i in range(n):
    for j in range(i+1):
        res += p[j]
print(res)
